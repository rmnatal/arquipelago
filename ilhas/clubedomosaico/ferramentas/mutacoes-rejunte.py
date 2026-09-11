#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra o banco de rejunte de proposito, uma mutacao por vez, e exige que
`validar-banco.py` REPROVE cada uma.

    python3 ferramentas/mutacoes-rejunte.py

Por que este arquivo existe: a secao 8 do ARQUIPELAGO.md diz que teste verde que nunca
foi visto reprovar nao mediu nada, e que a trava so vale depois de alguem tentar passar
por baixo dela. As travas do bloco 3c ficaram verdes na PRIMEIRA execucao — o que e bom
sinal e prova nenhuma. Cada mutacao abaixo e uma forma plausivel de o banco ficar errado
em silencio, e o que se mede aqui e se a regua enxerga.

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


def material(banco, ident):
    for m in banco["materiais"]:
        if m["id"] == ident:
            return m
    raise KeyError(ident)


# ------------------------------------------------------------------ mutacoes
# Cada uma recebe a raiz da copia e a altera. O nome diz o que ela finge ser.

def m_junta_um_milimetro_a_mais(raiz):
    """O erro de digitacao mais banal que existe: 4 vira 5 na faixa do acrilico.

    E o que a grade de passo fixo nao pegaria. So pega quem pisa na borda."""
    b = carregar(raiz, "materiais-rejuntes.json")
    material(b, "quartzolit-rejunte-acrilico")["propriedades"]["junta_max_mm"]["valor"] = 5
    gravar(raiz, "materiais-rejuntes.json", b)


def m_faixa_pela_metade(raiz):
    """Alguem obtem so o minimo e deixa o maximo null, achando que virou 'sem limite'."""
    b = carregar(raiz, "materiais-rejuntes.json")
    p = material(b, "quartzolit-rejunte-epoxi")["propriedades"]
    p["junta_max_mm"] = {"valor": None, "unidade": "mm", "motivo": "nao obtido"}
    gravar(raiz, "materiais-rejuntes.json", b)


def m_faixa_invertida(raiz):
    """Minimo e maximo trocados de lugar."""
    b = carregar(raiz, "materiais-rejuntes.json")
    p = material(b, "quartzolit-rejunte-ceramicas")["propriedades"]
    p["junta_min_mm"]["valor"], p["junta_max_mm"]["valor"] = 10, 2
    gravar(raiz, "materiais-rejuntes.json", b)


def m_piscinas_ganha_junta_inventada(raiz):
    """A tentacao mais forte deste bloco: o unico produto declarado para pastilha de vidro
    submersa esta fora da grade por falta da faixa de junta. Inventar 1 a 5 mm para ele
    'funcionar' e exatamente o que a regra 1 existe para impedir."""
    b = carregar(raiz, "materiais-rejuntes.json")
    p = material(b, "quartzolit-rejunte-piscinas")["propriedades"]
    p["junta_min_mm"] = {"valor": 1, "unidade": "mm", "fonte_id": "pagina-produto-rejunte-piscinas",
                         "declarado_como": "inventado pela mutacao"}
    p["junta_max_mm"] = {"valor": 5, "unidade": "mm", "fonte_id": "pagina-produto-rejunte-piscinas",
                         "declarado_como": "inventado pela mutacao"}
    gravar(raiz, "materiais-rejuntes.json", b)


def m_epoxi_perde_a_piscina(raiz):
    """Some a declaracao de piscina do epoxi. A celula de 3 mm submersa deveria esvaziar."""
    b = carregar(raiz, "materiais-rejuntes.json")
    d = material(b, "quartzolit-rejunte-epoxi")["declaracoes"]
    d["indicado_para"] = ["uso residencial, comercial e industrial", "paredes e pisos"]
    d["resistencias_declaradas"] = ["impermeavel, antimofo e resistente a manchas"]
    gravar(raiz, "materiais-rejuntes.json", b)


def m_ambiente_generico_vira_declaracao(raiz):
    """A porta dos fundos do mapa: fazer 'areas internas e externas' cobrir externo_exposto.

    Se passar, qualquer escopo comercial generico satisfaz sozinho a regra do ambiente
    critico, e sol e chuva deixam de exigir declaracao por nome."""
    e = carregar(raiz, "esquema-banco.json")
    for termo in e["mapa_de_termos_do_rejunte"]["termos"]:
        if termo["literal"] == "areas internas e externas":
            termo["ambiente"] = ["interno_seco", "interno_molhado",
                                 "externo_abrigado", "externo_exposto"]
    gravar(raiz, "esquema-banco.json", e)


def m_grade_sem_borda(raiz):
    """A grade deixa de pisar em 4 mm, que e o maximo do acrilico. Ela continua com nove
    celulas e com cara de grade — e para de separar 'ate 4' de 'ate 5'."""
    e = carregar(raiz, "esquema-banco.json")
    for celula in e["matriz_esperada_do_rejunte"]["celulas"]:
        if celula["junta_mm"] == 4:
            celula["junta_mm"] = 3
            celula["recomendados_topo"] = ["quartzolit-rejunte-acrilico",
                                           "quartzolit-rejunte-ceramicas",
                                           "quartzolit-rejunte-epoxi",
                                           "quartzolit-rejunte-porcelanatos-e-ceramicas"]
    gravar(raiz, "esquema-banco.json", e)


def m_rejunte_invade_a_matriz_da_cola(raiz):
    """Desfaz o conserto deste bloco: a matriz da F2 volta a olhar o banco inteiro."""
    e = carregar(raiz, "esquema-banco.json")
    e["matriz_esperada_da_F2"]["categoria_considerada"] = "rejunte"
    gravar(raiz, "esquema-banco.json", e)


def m_nivel_de_blog_vira_recomendacao(raiz):
    """O boletim do epoxi some e sobra a materia de blog, nivel 4. Ele deveria cair de
    recomendado para mencao com ressalva, nunca continuar no topo."""
    b = carregar(raiz, "materiais-rejuntes.json")
    m = material(b, "quartzolit-rejunte-epoxi")
    m["fontes"] = {"blog-fabricante-rejunte-epoxi": m["fontes"]["blog-fabricante-rejunte-epoxi"]}
    for prop in m["propriedades"].values():
        if prop.get("fonte_id") == "bt-rejunte-epoxi-2018-01":
            prop["fonte_id"] = "blog-fabricante-rejunte-epoxi"
    gravar(raiz, "materiais-rejuntes.json", b)


def m_rejunte_sem_perfil_escrito(raiz):
    """Entra um rejunte novo no banco e ninguem escreve o perfil esperado dele no esquema.
    Sem esta trava, ele passaria a influenciar a matriz sem nunca ter sido conferido."""
    b = carregar(raiz, "materiais-rejuntes.json")
    novo = json.loads(json.dumps(material(b, "quartzolit-rejunte-acrilico")))
    novo["id"] = "rejunte-fantasma"
    b["materiais"].append(novo)
    b["afiliado"]["itens_esperando_link"] = 6
    b["imagens"]["itens_sem_imagem"] = 6
    gravar(raiz, "materiais-rejuntes.json", b)


def m_cabecalho_mente_sobre_link(raiz):
    """O cabecalho declara menos itens esperando link do que o arquivo tem — o numero que
    a secao 7 do contrato manda reportar em todo bloco."""
    b = carregar(raiz, "materiais-rejuntes.json")
    b["afiliado"]["itens_esperando_link"] = 2
    gravar(raiz, "materiais-rejuntes.json", b)


def m_epoxi_perde_a_piscina_com_perfil_ajustado(raiz):
    """A MESMA mutacao de cima, so que feita por alguem cuidadoso: ele tira a declaracao
    do banco E acerta o perfil esperado no esquema, que e como um editor de verdade mexe
    nas duas metades. A comparacao de perfil passa a bater, porque as duas metades erraram
    juntas — e a unica coisa que ainda pode ver e a MATRIZ, que continua esperando o epoxi
    no topo da celula de 3 mm submersa. Se esta passar, a conferencia de perfil e enfeite."""
    m_epoxi_perde_a_piscina(raiz)
    e = carregar(raiz, "esquema-banco.json")
    for p in e["perfis_esperados_do_rejunte"]["perfis"]:
        if p["id"] == "quartzolit-rejunte-epoxi":
            p["ambientes_cobertos"] = []
    gravar(raiz, "esquema-banco.json", e)


MUTACOES = [
    ("junta com 1 mm a mais no acrilico", m_junta_um_milimetro_a_mais),
    ("faixa de junta pela metade", m_faixa_pela_metade),
    ("faixa de junta invertida", m_faixa_invertida),
    ("faixa de junta inventada para o rejunte piscinas", m_piscinas_ganha_junta_inventada),
    ("epoxi perde a declaracao de piscina", m_epoxi_perde_a_piscina),
    ("epoxi perde a piscina E o perfil e ajustado junto", m_epoxi_perde_a_piscina_com_perfil_ajustado),
    ("ambiente generico passa a cobrir sol e chuva", m_ambiente_generico_vira_declaracao),
    ("grade deixa de pisar na borda de 4 mm", m_grade_sem_borda),
    ("rejunte volta a entrar na matriz da cola", m_rejunte_invade_a_matriz_da_cola),
    ("fonte de blog (nivel 4) sustentando recomendacao", m_nivel_de_blog_vira_recomendacao),
    ("rejunte novo sem perfil esperado escrito", m_rejunte_sem_perfil_escrito),
    ("cabecalho mente sobre itens esperando link", m_cabecalho_mente_sobre_link),
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

    passaram = []
    for nome, mutar in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            mutar(copia)
            rc, saida = rodar_validador(copia)
            if rc == 0:
                passaram.append(nome)
                print("  PASSOU (a trava NAO viu): %s" % nome)
            else:
                primeira = ""
                for linha in saida.splitlines():
                    if linha.strip().startswith("- "):
                        primeira = linha.strip()[2:]
                        break
                print("  reprovou como devia: %-52s | %s" % (nome, primeira[:96]))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    print("\n%d mutacoes, %d reprovadas, %d passaram" %
          (len(MUTACOES), len(MUTACOES) - len(passaram), len(passaram)))
    if passaram:
        print("\nAS QUE PASSARAM SAO O RESULTADO DO TESTE, nao um detalhe:")
        for nome in passaram:
            print("  - %s" % nome)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

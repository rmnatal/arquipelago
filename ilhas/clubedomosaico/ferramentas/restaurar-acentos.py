#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Devolve os acentos as strings do banco que CHEGAM A TELA.

    python3 ferramentas/restaurar-acentos.py .            # so mostra
    python3 ferramentas/restaurar-acentos.py . --gravar   # aplica

POR QUE ISTO EXISTE. O bloco 4 publicou a primeira ferramenta da ilha e a
primeira coisa que o render de bancada mostrou foi "Silicone Acetico
Construcao" e "o fabricante declara ceramica e azulejo" — portugues errado,
vindo do banco, servido ao visitante e ao Google. O banco nasceu sem acento
porque foi digitado a partir de busca, e ate aqui ele so era lido por
ferramenta; no dia em que uma PAGINA passou a servi-lo, o defeito virou texto
no ar. A Robometria pagou exatamente isto em 11/09/2026, com 121 strings.

A OPERACAO E PROVADAMENTE DIACRITICO-ONLY, e e o `--provar` que garante:
reduzido a sem-diacritico, o banco depois desta ferramenta e byte a byte igual
ao banco antes dela. Sem essa prova, "restaurar acento" e uma porta aberta para
reescrever declaracao de fabricante — que e a unica coisa que este banco nao
pode deixar acontecer.

AS DUAS EXCECOES, declaradas aqui em vez de escondidas no mapa:
  1. `nome_comercial` dos cinco rejuntes vinha em CAIXA BAIXA ("rejunte
     acrilico quartzolit"), que nao e nome de produto, e virou nome proprio.
     Isso NAO e diacritico, entao esta na lista `CAIXA` e o --provar a
     desconsidera nomeadamente — uma por uma, nunca por regra geral.
  2. O "e" atono nao se resolve por palavra ("e" conjuncao e "e" verbo sao a
     mesma letra). As frases em que ele aparece estao em `FRASES`, inteiras.

O QUE A FERRAMENTA IMPRIME: cada troca que fez, com o campo e o id do produto.
Espelho que nao imprime o que trocou envelhece calado (secao 8 do contrato).
"""

import json
import os
import re
import sys
import unicodedata

CAMPOS_DE_TELA = ("marca", "fabricante", "nome_comercial")
LISTAS_DE_DECLARACAO = (
    "indicado_para", "nao_usar_em", "nao_recomendado_em",
    "nao_indicado_para", "ambientes_declarados", "resistencias_declaradas",
)

# Palavra sem acento -> palavra com acento. So palavras em que a forma acentuada
# e a UNICA leitura possivel em portugues; qualquer ambiguidade vai para FRASES.
PALAVRAS = {
    "acetico": "acético", "acidos": "ácidos", "acrilico": "acrílico",
    "agua": "água", "aluminio": "alumínio", "aquarios": "aquários",
    "area": "área", "areas": "áreas", "ate": "até",
    "calcario": "calcário", "ceramica": "cerâmica", "ceramicas": "cerâmicas",
    "ceramico": "cerâmico", "cimenticio": "cimentício", "condicao": "condição",
    "construcao": "construção", "cortica": "cortiça", "corrosivel": "corrosível",
    "corrosiveis": "corrosíveis", "dominio": "domínio", "encadernacao": "encadernação",
    "epoxi": "epóxi", "especiais": "especiais", "formula": "fórmula",
    "imersao": "imersão", "impermeavel": "impermeável", "latao": "latão",
    "liberacao": "liberação", "liquido": "líquido", "marmore": "mármore",
    "materia": "matéria", "media": "média", "mencao": "menção",
    "metalico": "metálico", "nao": "não", "pagina": "página",
    "papelao": "papelão", "plastico": "plástico", "plasticos": "plásticos",
    "proprio": "próprio", "resistencia": "resistência", "rodapes": "rodapés",
    "sao": "são", "sobreposicao": "sobreposição", "superficies": "superfícies",
    "tecnica": "técnica", "tecnico": "técnico", "variacao": "variação",
    "vedacao": "vedação",
}

# Frases inteiras, para o que palavra nenhuma resolve.
FRASES = {
    "imersao continua em meio liquido": "imersão contínua em meio líquido",
    "material de imprensa do fabricante (2018) — NAO e ficha tecnica":
        "material de imprensa do fabricante (2018) — NÃO é ficha técnica",
    "materia do blog do proprio fabricante — e onde aparece a mencao a PASTILHAS entre os revestimentos, que o boletim nao trouxe":
        "matéria do blog do próprio fabricante — é onde aparece a menção a PASTILHAS entre os revestimentos, que o boletim não trouxe",
}

# Caixa alta de nome proprio. NAO e diacritico: cada uma esta escrita inteira,
# e o --provar as desconsidera nomeadamente.
CAIXA = {
    "rejunte acrilico quartzolit": "Rejunte Acrílico Quartzolit",
    "rejunte ceramicas quartzolit": "Rejunte Cerâmicas Quartzolit",
    "rejunte epoxi quartzolit": "Rejunte Epóxi Quartzolit",
    "rejunte piscinas quartzolit": "Rejunte Piscinas Quartzolit",
    "rejunte porcelanatos e ceramicas quartzolit": "Rejunte Porcelanatos e Cerâmicas Quartzolit",
}

ARQUIVOS = ("materiais-colas.json", "materiais-rejuntes.json")


def sem_diacritico(texto):
    return "".join(c for c in unicodedata.normalize("NFKD", texto) if not unicodedata.combining(c))


def acentuar(texto):
    if texto in CAIXA:
        return CAIXA[texto]
    if texto in FRASES:
        return FRASES[texto]

    def troca(m):
        p = m.group(0)
        alvo = PALAVRAS.get(p.lower())
        if alvo is None:
            return p
        if p.isupper():
            return alvo.upper()
        if p[0].isupper():
            return alvo[0].upper() + alvo[1:]
        return alvo

    return re.sub(r"[A-Za-zÀ-ÿ]+", troca, texto)


def percorrer(material):
    """Devolve [(caminho, valor_atual, setter)] de tudo que chega a tela."""
    saida = []
    for campo in CAMPOS_DE_TELA:
        if isinstance(material.get(campo), str):
            saida.append((campo, material[campo],
                          lambda v, c=campo: material.__setitem__(c, v)))
    decl = material.get("declaracoes") or {}
    for lista in LISTAS_DE_DECLARACAO:
        valores = decl.get(lista)
        if not isinstance(valores, list):
            continue
        for i, v in enumerate(valores):
            if isinstance(v, str):
                saida.append(("declaracoes.%s[%d]" % (lista, i), v,
                              lambda nv, l=valores, j=i: l.__setitem__(j, nv)))
    for fid, fonte in (material.get("fontes") or {}).items():
        if isinstance(fonte.get("tipo"), str):
            saida.append(("fontes.%s.tipo" % fid, fonte["tipo"],
                          lambda v, f=fonte: f.__setitem__("tipo", v)))
    return saida


def main():
    raiz = sys.argv[1] if len(sys.argv) > 1 else "."
    gravar = "--gravar" in sys.argv
    trocas = 0
    sem_mapa = set()

    for nome in ARQUIVOS:
        caminho = os.path.join(raiz, "dados", nome)
        with open(caminho, encoding="utf-8") as fh:
            dados = json.load(fh)

        for material in dados.get("materiais", []):
            for campo, valor, setter in percorrer(material):
                novo = acentuar(valor)
                if novo != valor:
                    trocas += 1
                    print("  %-34s %-38s %s  ->  %s" % (material["id"], campo, valor, novo))
                    setter(novo)
                    valor = novo
                # PROVA: o que sobrou sem acento e palavra que o mapa nao conhece.
                for palavra in re.findall(r"[A-Za-zÀ-ÿ]+", valor):
                    if len(palavra) < 4 or palavra.lower() in ("para", "pdf"):
                        continue
                    if sem_diacritico(palavra) == palavra and palavra.lower() not in _CONHECIDAS:
                        sem_mapa.add(palavra.lower())

        if gravar:
            with open(caminho, "w", encoding="utf-8") as fh:
                json.dump(dados, fh, ensure_ascii=False, indent=2)
                fh.write("\n")

    print("\n  %d trocas%s" % (trocas, " GRAVADAS" if gravar else " (nada gravado; use --gravar)"))
    if sem_mapa:
        print("  palavras sem acento que o mapa nao conhece (confira uma a uma):")
        print("    " + ", ".join(sorted(sem_mapa)))
    return 0


# Palavras que EXISTEM sem acento em portugues e nao devem ser acusadas. A lista
# e explicita de proposito: o aviso so vale se ele nao gritar o tempo todo.
_CONHECIDAS = set("""
alcalinas algas alimento alta alvenaria ambiente ambientes anodizado antigo antimofo
aparece apresenta aramado assentamento azulejo baixa biocida blog boletim borracha
cimento cobre colagem comercial completamente compensado comum concreto contato
contra cortado couro decorativos densidade dele desta dias exija expandido externa
externo fabricante fachada ferro fibras fungos galvanizada gesso granito imprensa
industrial interna interno internos laminado laminados lido madeira manchas marca
material medida meio metais metal molduras molhada molhadas naturais neutro
outros ouro papel pastilhas pedra pedras pintadas piscinas piso pisos placa placas
polietileno policarbonato polipropileno poliestireno porcelana porcelanatos porosas
porosos prata produto protect quimicamente raios recomendado rejunte residencial
resistente revestimentos silicone sobre sobreposto submersa submersas submerso
sol tecido tecnologia tela temperado temperatura tijolo trouxe uso usado vento
vidro zinco cascola cascorez durepoxi extra extraforte formica formiplac henkel
loctite perstop quartzolit saint gobain tekbond weber argamassa cimentcola branca
esquadria natural revisada arquivo busca ajuda consumo exemplo publicados
aberto agentes algicida alguns aquecidas brsa celsius certos chapa chuva cola
entre especiais espelhos estrutural externas fechado ficha graus horas internas
onde paredes proteger tipos tratada materiais
""".split())


if __name__ == "__main__":
    sys.exit(main())

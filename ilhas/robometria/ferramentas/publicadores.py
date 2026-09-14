#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A GRAMATICA DE QUEM PUBLICA, num lugar so (14/09/2026).

    python3 ferramentas/publicadores.py        # imprime a tabela e sai

POR QUE ESTE ARQUIVO EXISTE
---------------------------
Ate 14/09/2026 o artigo que vem antes do nome de quem publicou era DIGITADO
dentro de cada frase — "A %s declara", "que a %s declara", "a %s declara esta
peca", " da " antes do nome no artigo-ancora — e funcionava porque todo
publicador que chegava aquelas frases e feminino singular. Era verdadeiro por
ACIDENTE DO BANCO, da mesma familia do "o fabricante declara" que o bloco das
11h44Z tirou do ar: uma frase que nasce certa na primeira pagina e vai errada
para a do lado.

O banco ja tinha os dois contraexemplos, e nenhum deles passava por uma frase
com artigo: "Mundo Conectado" e MASCULINO (a R2 ja escrevia "o Mundo Conectado",
por uma segunda tabela digitada dentro de ferramentas/cobertura-r2.py) e "Lojas
WAP" e PLURAL, e nenhuma frase o cita ate hoje. Regua escrita para um mundo que
nunca aconteceu nasce errada sem poder falhar (secao 8 do ARQUIPELAGO.md).

A REGRA QUE SOBRA: o artigo e DADO, declarado ao lado do nome em
dados/publicadores.json; o que se DERIVA dele — maiuscula de comeco de frase,
contracao com "de", pronome possessivo e numero do verbo — mora em
artigos_de_publicador, no esquema. Quem monta frase le daqui, e nenhuma das duas
tabelas volta para dentro de um snippet ou de um gerador.

E A FALTA PARA A EXECUCAO, em vez de publicar concordancia adivinhada: publicador
sem registro derruba o gerador com o nome dele na mensagem. E o mesmo tratamento
que ROTULOS_DE_ORIGEM ja dava a origem sem rotulo de tela desde 11/09.
"""

import json
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")


def _carregar(nome):
    with open(os.path.join(DADOS, nome), encoding="utf-8") as fh:
        return json.load(fh)


def _tabelas():
    esquema = _carregar("esquema-banco.json")
    artigos = esquema.get("artigos_de_publicador")
    if not isinstance(artigos, dict):
        sys.stderr.write(
            "ERRO: dados/esquema-banco.json nao declara artigos_de_publicador. "
            "Sem a tabela do esquema nao ha de onde derivar maiuscula, contracao "
            "nem numero do verbo, e a frase voltaria a adivinhar.\n")
        sys.exit(1)

    banco = _carregar("publicadores.json")
    por_nome = {}
    for reg in banco["registros"]:
        artigo = reg.get("artigo")
        forma = artigos.get(artigo)
        if not isinstance(forma, dict):
            sys.stderr.write(
                "ERRO: o publicador %r declara o artigo %r, que nao existe em "
                "artigos_de_publicador.\n" % (reg.get("nome"), artigo))
            sys.exit(1)
        registro = dict(forma)
        registro["artigo"] = artigo
        registro["nome"] = reg["nome"]
        registro["id"] = reg["id"]
        por_nome[reg["nome"]] = registro
    return artigos, por_nome


ARTIGOS, POR_NOME = _tabelas()


def gramatica(publicador):
    """Tudo o que uma frase precisa saber sobre este nome, ou a execucao para.

    Parar e a parte importante. A alternativa — cair num artigo padrao quando o
    nome nao esta declarado — publica a concordancia errada em silencio, no meio
    de uma oracao que a pagina AFIRMA, e e exatamente o defeito que esta tabela
    existe para impedir.
    """
    g = POR_NOME.get(publicador)
    if g is None:
        sys.stderr.write(
            "ERRO: o publicador %r nao tem registro em dados/publicadores.json. "
            "Declare o artigo dele (e o motivo) antes de publicar qualquer frase "
            "que o ponha como sujeito: artigo adivinhado do nome erra em 'Mundo "
            "Conectado' e em 'Lojas WAP', que o banco ja tem.\n" % (publicador,))
        sys.exit(1)
    return g


def com_artigo(publicador):
    """'a Electrolux (loja oficial)', 'o Mundo Conectado', 'as Lojas WAP'."""
    return "%s %s" % (gramatica(publicador)["artigo"], publicador)


def com_artigo_maiusculo(publicador):
    """O mesmo, abrindo frase. A maiuscula vem do esquema e nao de capitalize():
    'as' vira 'As', e nenhuma funcao de string sabe disso sozinha."""
    return "%s %s" % (gramatica(publicador)["maiuscula"], publicador)


def com_de(publicador):
    """'da Electrolux', 'do Mundo Conectado', 'das Lojas WAP'."""
    return "%s %s" % (gramatica(publicador)["com_de"], publicador)


def verbo(publicador, singular, plural):
    """'declara' / 'declaram', pelo numero DECLARADO de quem publica."""
    return plural if gramatica(publicador)["numero"] == "plural" else singular


def pronome_possessivo(publicador):
    """'dela' / 'dele' / 'delas' / 'deles'."""
    return gramatica(publicador)["pronome_possessivo"]


def main():
    print("Robometria — gramatica de quem publica")
    print("=" * 70)
    print("artigos declarados no esquema: %s" % ", ".join(sorted(ARTIGOS)
                                                          if isinstance(ARTIGOS, dict) else []))
    for nome in sorted(POR_NOME):
        g = POR_NOME[nome]
        print("  %-58s %-3s %-8s %s"
              % (nome, g["artigo"], g["numero"], g["pronome_possessivo"]))
    print("\n%d publicador(es) declarado(s)." % len(POR_NOME))


if __name__ == "__main__":
    main()

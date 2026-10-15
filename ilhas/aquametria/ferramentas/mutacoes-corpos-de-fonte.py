#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MUTACOES DELIBERADAS CONTRA O REGISTRO DE CORPOS DE FONTE (regra E26, 15/10/2026).

    python3 ferramentas/mutacoes-corpos-de-fonte.py

O mutante e `validar-especies.py` (e, numa das mutacoes, o proprio esquema), e quem
tem de reprovar e `testar-validador-especies.py`, com codigo de saida 1 e sem
traceback.

POR QUE ELE EXISTE, E A CAUSA FOI MEDIDA HOJE E NAO SUPOSTA. Ate 15/10/2026 quem
decidia "corpo de fonte distinto" era o HOSTNAME, por uma tabela de espelhos escrita
no codigo e COPIADA A MAO num segundo arquivo. Espelho ela pegava — mesma FishBase em
dois dominios. REPRODUTOR nao: o corpo que republica o numero de outro mora num host
que a tabela nao tem, e assim ele faria um registro de corpo UNICO passar por
conferido, que e exatamente o que o E15 existe para impedir, um andar acima.

E O CASO NAO ERA HIPOTETICO — ele apareceu na mesa nesta mesma execucao. O proximo
passo desbloqueado da ilha era fechar o `aviso [E15] poecilia-reticulata` (o guppy tem
duas urls e um corpo so), e a busca restrita achou um candidato de verdade: a ficha de
Poecilia reticulata do Nonindigenous Aquatic Species Database do USGS, que publica
"males to 2.5 cm SL; females to 6 cm SL" atribuido a especie PELO NOME. Ele passa na
regra_de_atribuicao_por_busca da escada e seria o segundo corpo que falta. FOI
RECUSADO porque a ficha nao nomeia o estudo primario do numero, e corpo cuja
procedencia nao se mede pode estar reproduzindo a FishBase — o unico corpo que esse
registro tem. Se ele tivesse entrado, o `aviso [E15]` ficaria MUDO e o E14 deixaria o
guppy virar `completo` sobre um corpo so. A regua nao tinha como dizer isso, e agora
tem: `corpos_de_fonte` declara cada corpo, os hosts dele e a procedencia do numero.

O QUE CADA METADE MEDE, porque cada uma sozinha aprova um mundo errado diferente: a
DECLARACAO obrigatoria sozinha deixaria um reprodutor declarado contar como corpo
proprio; a CONTAGEM por procedencia sozinha nao impediria um corpo novo de entrar sem
ninguem decidir o que ele e.

A MUTACAO 4 TEM DUAS EDICOES, e a segunda e o MUNDO, nunca uma segunda regra (secao 8
do ARQUIPELAGO.md, a mesma autorizacao que a mutacao 7 do mutacoes-alvo-dos-casos.py
usou). O ramo `reproduz` nao tem ocupante no esquema de hoje — nenhum corpo esta
declarado como reprodutor —, entao afrouxa-lo nao quebra nada enquanto o mundo nao
existir. A primeira edicao do esquema PRODUZ esse mundo, declarando o usgs-nas como
reprodutor da FishBase; a segunda e a regra afrouxada.
"""
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTAO = "ferramentas/testar-validador-especies.py"
VALIDADOR = "ferramentas/validar-especies.py"
ESQUEMA = "dados/esquema-especies.json"


def troca(arquivo, pares, vezes=1):
    """Substituicoes exatas que RECUSAM operar se o alvo nao estiver la.

    E a trava contra a mutacao inerte: alvo que nao existe mais nao quebra nada e a
    mutacao passa por engano — 18 de 20 mutacoes desta ilha viraram inertes de uma vez
    em 11/09/2026, quando a bancada trocou de fonte.
    """
    def aplicar(base):
        caminho = os.path.join(base, arquivo)
        texto = open(caminho, encoding="utf-8").read()
        for de, para in pares:
            if texto.count(de) != vezes:
                raise SystemExit("MUTACAO INERTE: %r aparece %d vez(es) em %s, esperava %d"
                                 % (de, texto.count(de), arquivo, vezes))
            texto = texto.replace(de, para, vezes)
        open(caminho, "w", encoding="utf-8").write(texto)
    return aplicar


def duas(primeira, segunda):
    def aplicar(base):
        primeira(base)
        segunda(base)
    return aplicar


# O MUNDO da mutacao 4: o esquema passa a declarar um corpo REPRODUTOR, que ele nao tem
# hoje. Sozinha, esta edicao nao muda veredito nenhum — reprodutor colapsado no corpo
# que ele reproduz conta igual a corpo que nao conta.
DECLARA_REPRODUTOR = troca(ESQUEMA, [
    ('    "procedencia": "indeterminada",\n    "reproduz": null,',
     '    "procedencia": "reproduz",\n    "reproduz": "fishbase",'),
])

MUTACOES = [
 ("1. a contagem volta a sair do HOSTNAME, como ate 15/10/2026",
  "a regra inteira, e esta mutacao E o codigo de ontem em pessoa: host diferente "
  "contando como corpo diferente, sem olhar declaracao nem procedencia. Ela mede as "
  "tres travas de uma vez",
  troca(VALIDADOR, [
      ('    corpo = corpo_declarado(url)\n    if corpo is None:\n        return None\n'
       '    if corpo["procedencia"] == "reproduz":',
       '    return host_da_fonte(url)  # MUTACAO\n'
       '    corpo = corpo_declarado(url)\n    if corpo is None:\n        return None\n'
       '    if corpo["procedencia"] == "reproduz":')])),

 ("2. corpo de procedencia `indeterminada` passa a contar como corpo proprio",
  "a metade da CONTAGEM, e e o caso que esta execucao recusou na mesa: fonte que nao "
  "diz de onde veio o numero dela nao e o proprio corpo (nao se sabe se e dele) nem o "
  "de outro (nao se sabe de quem e). Contando, ela promove um registro de corpo unico a "
  "conferido",
  troca(VALIDADOR, [
      ('    if corpo["procedencia"] == "indeterminada":\n        return None\n', '')])),

 ("3. a cobranca do E26 e removida: corpo nao declarado deixa de reprovar",
  "a metade da DECLARACAO. Sem ela, corpo novo entra calado e ninguem decide o que ele "
  "e — que e como o reprodutor passaria pela regua sem nunca ser olhado",
  troca(VALIDADOR, [
      ('            if corpo is None:\n                erro("E26", rid,',
       '            if False:  # MUTACAO\n                erro("E26", rid,')])),

 ("4. `reproduz` conta como si em vez de colapsar (duas edicoes: a 1a PRODUZ o mundo)",
  "o colapso do reprodutor, que e o buraco que esta regra nasceu para tapar. Duas urls "
  "de hosts diferentes servindo o numero do mesmo corpo continuam sendo UM corpo; sem o "
  "colapso, acrescentar um reprodutor faz o E15 calar e o E14 aprovar",
  duas(DECLARA_REPRODUTOR,
       troca(VALIDADOR, [('        return corpo.get("reproduz")',
                          '        return corpo["nome"]  # MUTACAO')]))),

 ("5. o host deixa de ser normalizado (o 'www.' nao e removido)",
  "a normalizacao do host, que nao e detalhe: as urls deste banco sao escritas com "
  "`www.` e os `hosts` do esquema sem. Sem ela nenhum corpo e encontrado, todo registro "
  "cai no E26 e o banco REAL para de passar — e era por isto que a copia a mao do "
  "varrer-categorias-possiveis.py listava as variantes com `www.` uma a uma",
  troca(VALIDADOR, [
      ('    return host[4:] if host.startswith("www.") else host',
       '    return host  # MUTACAO')])),
]


def main():
    print("== mutacoes contra o registro de corpos de fonte (E26) ==")
    falhas = []
    for titulo, porque, aplicar in MUTACOES:
        base = tempfile.mkdtemp(prefix="aqm-corpos-mut-")
        copia = os.path.join(base, "ilha")
        shutil.copytree(RAIZ, copia, symlinks=True,
                        ignore=shutil.ignore_patterns("node_modules", ".git", "__pycache__"))
        aplicar(copia)
        # sys.dont_write_bytecode no filho: a mutacao troca poucos caracteres e o .pyc do
        # original pode sobreviver a validacao de mtime + tamanho do Python, que custou um
        # diagnostico inteiro em 15/10/2026 no portao do search-console.py.
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        r = subprocess.run([sys.executable, os.path.join(copia, PORTAO)],
                           capture_output=True, text=True, cwd=copia, env=env)
        reprovou = r.returncode == 1
        limpo = "Traceback" not in (r.stdout + r.stderr)
        ok = reprovou and limpo
        print("  %-78s %s" % (titulo, "reprovou" if ok else "SOBREVIVEU"))
        if not ok:
            detalhe = "codigo de saida %d" % r.returncode
            if not limpo:
                detalhe += " e traceback (o portao morreu em vez de reprovar)"
            print("      %s" % detalhe)
            print("      para que a trava serve: %s" % porque)
            falhas.append(titulo)
        shutil.rmtree(base, ignore_errors=True)

    print("\n== resultado ==")
    print("  %d mutacao(oes), %d sobrevivente(s)" % (len(MUTACOES), len(falhas)))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

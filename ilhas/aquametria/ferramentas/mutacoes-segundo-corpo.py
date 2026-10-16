#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MUTACOES DELIBERADAS CONTRA A REGUA DO SEGUNDO CORPO QUE NAO ENTROU (E28, 16/10/2026).

    python3 ferramentas/mutacoes-segundo-corpo.py

O mutante e `validar-especies.py` (e, numa delas, o proprio `esquema-especies.json`) e
quem tem de reprovar e `testar-validador-especies.py`, com codigo de saida 1 e sem
traceback.

POR QUE ELA EXISTE. A E19 cuida da coleta que nao entrou em campo VAZIO desde 22/09/2026,
e tem dentes nisso: recusa de campo preenchido e erro. O terceiro caso apareceu inteiro
no dia em que a E27 passou a contar corpo POR CAMPO — o campo esta preenchido por UM
corpo, a execucao vai buscar o SEGUNDO e o segundo nao entra. Sem lugar para isso, o
achado vira prosa no REGISTRO.md e a execucao seguinte refaz a mesma busca.

O QUE CADA MUTACAO MEDE. A 1 e a regra inteira. A 2 e a FRONTEIRA com a E19, que e a
metade nova: sem ela as duas listas aceitam o mesmo registro e param de contar coisas
diferentes. A 3 e a 4 sao as duas maneiras de a decisao adiada perder a data — tirar a
exigencia, e tira-la so do desfecho que foi descoberto depois (`confirmou-espera-data`,
que e justamente o caso em que a fonte CONFIRMA e por isso parece inofensivo). A 5 tira
o vocabulario fechado. A 6 e a 7 sao o aviso que cobra o calendario: removido, e adiado
em um dia — e o dia que ele perde e exatamente o dia da decisao. A 8 nao mexe no
validador: ela acrescenta uma palavra ao vocabulario do ESQUEMA, e e ela que prova que a
conferencia entre as duas copias nao e decorativa.
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
    mutacao passa por engano.
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


MUTACOES = [
 ("1. a regra inteira deixa de olhar as entradas",
  "a E28 toda: a lista continua no banco, o campo continua no esquema e nada mais e "
  "conferido",
  troca(VALIDADOR, [
      ('        for i, c in enumerate(r.get("segundo_corpo_nao_entrou", []) or []):',
       '        for i, c in enumerate([]):  # MUTACAO')])),

 ("2. a fronteira com a E19 cai: segundo corpo de campo VAZIO passa",
  "a metade que faltava da fronteira entre as duas listas. A E19 ja reprovava recusa de "
  "campo preenchido; sem esta, nada reprova segundo corpo de campo vazio e a execucao "
  "escolhe a lista pelo gosto — duas listas que aceitam o mesmo registro contam a mesma "
  "coisa duas vezes em vez de contar duas coisas",
  troca(VALIDADOR, [
      ('                elif not preenchido(r.get(campo)):',
       '                elif False:  # MUTACAO')])),

 ("3. decisao adiada deixa de exigir data",
  "a trava que impede a divergencia de virar promessa sem prazo: sem ela a entrada fica "
  "no banco para sempre e nenhuma passada futura sabe quando decidir",
  troca(VALIDADOR, [
      ('            if desfecho in PEDEM_DATA and not decidir and not superada:',
       '            if False:  # MUTACAO')])),

 ("4. so `divergiu` passa a exigir data, e `confirmou-espera-data` fica de fora",
  "o desfecho que foi descoberto DEPOIS, e o mais silencioso dos dois: ali a fonte "
  "CONFIRMA o numero, entao a entrada parece inofensiva — e e justamente ela que espera "
  "so o calendario e some se nao tiver data",
  troca(VALIDADOR, [
      ('PEDEM_DATA = ("divergiu", "confirmou-espera-data")',
       'PEDEM_DATA = ("divergiu",)  # MUTACAO')])),

 ("5. o vocabulario do desfecho deixa de ser fechado",
  "o vocabulario: com ele aberto, 'nao deu certo' entra como desfecho e as quatro causas "
  "— que pedem coisas diferentes de quem for resolve-las — viram uma pilha so",
  troca(VALIDADOR, [
      ('            if desfecho not in DESFECHOS_SEGUNDO_CORPO:',
       '            if False:  # MUTACAO')])),

 ("6. o aviso do prazo vencido some",
  "a unica parte desta regra que cobra o CALENDARIO. Sem ela a divergencia envelhece "
  "calada enquanto a tela segue publicando um numero so, que e a licao da 25.4-b.3 do "
  "contrato aplicada ao banco de especies",
  troca(VALIDADOR, [
      ('                    if prazo <= hoje and not superada:',
       '                    if False:  # MUTACAO')])),

 ("7. o prazo passa a cobrar so no dia SEGUINTE ao da decisao",
  "a borda do prazo. O dia que o aviso perde e exatamente o dia marcado para decidir — o "
  "unico em que alguem estaria olhando para ela",
  troca(VALIDADOR, [
      ('                    if prazo <= hoje and not superada:',
       '                    if prazo < hoje and not superada:  # MUTACAO')])),

 ("8. o vocabulario do ESQUEMA ganha uma palavra que o validador nao conhece",
  "a conferencia entre as duas copias do vocabulario. Esta mutacao nao toca no "
  "validador: ela prova que a lista escrita duas vezes e conferida, e nao decorativa — "
  "sem a conferencia, qualquer palavra acrescentada ao esquema passaria a valer sem "
  "ninguem decidir, que e o buraco que o E26 tapou um andar abaixo",
  troca(ESQUEMA, [
      ('"nao-cobre": "o corpo declara que nao tem ficha desta especie.',
       '"talvez": "MUTACAO", "nao-cobre": "o corpo declara que nao tem ficha desta especie.')])),
]


def main():
    print("== mutacoes contra a regua do segundo corpo que nao entrou (E28) ==")
    falhas = []
    for titulo, porque, aplicar in MUTACOES:
        base = tempfile.mkdtemp(prefix="aqm-segundo-mut-")
        copia = os.path.join(base, "ilha")
        shutil.copytree(RAIZ, copia, symlinks=True,
                        ignore=shutil.ignore_patterns("node_modules", ".git", "__pycache__"))
        aplicar(copia)
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        r = subprocess.run([sys.executable, os.path.join(copia, PORTAO)],
                           capture_output=True, text=True, cwd=copia, env=env)
        reprovou = r.returncode == 1
        limpo = "Traceback" not in (r.stdout + r.stderr)
        ok = reprovou and limpo
        print("  %-74s %s" % (titulo, "reprovou" if ok else "SOBREVIVEU"))
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

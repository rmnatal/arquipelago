#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MUTACOES DELIBERADAS CONTRA A CONTAGEM DE CORPOS POR CAMPO (regra E27, 16/10/2026).

    python3 ferramentas/mutacoes-corpos-por-campo.py

O mutante e `validar-especies.py` e quem tem de reprovar e
`testar-validador-especies.py`, com codigo de saida 1 e sem traceback.

POR QUE ELA EXISTE, E A CAUSA FOI MEDIDA E NAO SUPOSTA. O E14 e o E15 contam os corpos
que o REGISTRO cita. Essa pergunta e sobre o SINTOMA — duas urls fingindo dois corpos —
e por isso aprova em silencio o mundo em que o sintoma nao aparece: o registro cita dois
corpos de verdade, o segundo sustenta so campo OPCIONAL, e todo campo obrigatorio
continua apoiado no primeiro. Varrido no banco em 16/10/2026: OITO registros caem nesse
estado. Dois deles (danio-margaritatus e poecilia-reticulata) ja eram visiveis um andar
acima; os outros SEIS nao eram vistos por regua nenhuma, e TRES desses seis sao
`completo` — paracheirodon-innesi, symphysodon-aequifasciatus e pterophyllum-scalare —,
ou seja o E14 aprovou o status pelo corpo que nao sustenta campo obrigatorio nenhum.

A FAMILIA DO DEFEITO E A MESMA QUE O E26 FECHOU NA VESPERA, um andar abaixo: la a
contagem saia do HOSTNAME e nao da procedencia; aqui ela saia do REGISTRO e nao do
CAMPO. Nos dois casos a regua respondia uma pergunta parecida com a certa, e o erro so
aparece no mundo em que as duas perguntas se separam.

O QUE CADA MUTACAO MEDE: a 1 e a regua de ontem em pessoa (contar o registro), a 2 e a 4
sao as duas maneiras de a contagem deixar de ser por CORPO (por fonte, e tratando
`indeterminada` como corpo), a 3 tira a metade de erro, a 5 derruba o limiar e a 6 troca
o nucleo obrigatorio pelo conjunto de todos os campos com fonte — que e o jeito mais
silencioso de a regra parar de medir o que ela promete, porque ela continua existindo e
nunca mais acusa.
"""
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTAO = "ferramentas/testar-validador-especies.py"
VALIDADOR = "ferramentas/validar-especies.py"


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


MUTACOES = [
 ("1. a contagem volta a ser a do REGISTRO, e nao a do CAMPO",
  "a regra inteira, e esta mutacao E a regua de ontem em pessoa: o nucleo passa a ser "
  "contado por quantos corpos o registro CITA, que e o que o E15 ja fazia. Com ela, o "
  "registro que cita dois corpos e apoia todo o nucleo em um volta a passar calado",
  troca(VALIDADOR, [
      ('            corpos_do_nucleo = set()\n'
       '            for campo in nucleo:\n'
       '                corpos_do_nucleo |= corpos_do_campo.get(campo, set())\n',
       '            corpos_do_nucleo = corpos_de(r)  # MUTACAO\n')])),

 ("2. a contagem passa a ser por FONTE e nao por CORPO",
  "o colapso de duas urls do mesmo corpo. Contando fonte, as duas fichas da FishBase do "
  "mesmo registro viram dois, e o nucleo apoiado numa base so passa por conferido — e "
  "duas urls do mesmo corpo e exatamente o defeito que o E15 nasceu para pegar",
  troca(VALIDADOR, [
      ('            if nome:\n                por_campo[campo].add(nome)',
       '            if nome:\n                por_campo[campo].add(f.get("url"))  # MUTACAO')])),

 ("3. a metade de ERRO e removida: campo sem corpo contavel deixa de reprovar",
  "a trava de que campo obrigatorio tem de ter CORPO e nao so FONTE. Sem ela, um campo "
  "sustentado so por fonte de procedencia indeterminada passa no E3 e fica sem ninguem "
  "que o sustente, que e o buraco que o E26 deixou um andar abaixo",
  troca(VALIDADOR, [
      ('            if not corpos_do_campo.get(campo):',
       '            if False:  # MUTACAO')])),

 ("4. `indeterminada` volta a contar como corpo nesta regua",
  "a procedencia, que e quem decide o que conta. Fonte que nao diz de onde veio o numero "
  "dela nao e o proprio corpo nem o de outro; contando, ela sustenta campo obrigatorio "
  "sozinha e a regua nova herda o palpite que o E26 tirou do hostname",
  troca(VALIDADOR, [
      ('        nome = corpo_contavel(f.get("url"))',
       '        nome = (corpo_declarado(f.get("url")) or {}).get("nome")  # MUTACAO')])),

 ("5. o limiar do aviso cai de dois corpos para um",
  "o limiar, e com ele o aviso inteiro: `< 1` nunca e verdade, porque registro sem corpo "
  "nenhum no nucleo ja cai na metade de erro. A regra continua no arquivo, continua "
  "rodando e nunca mais acusa",
  troca(VALIDADOR, [
      ('            if len(corpos_do_nucleo) < 2:',
       '            if len(corpos_do_nucleo) < 1:  # MUTACAO')])),

 ("6. o nucleo deixa de ser o dos campos OBRIGATORIOS e vira o de todos os campos",
  "o recorte da regra, que e o que a torna util: medida sobre todos os campos com fonte, "
  "ela e satisfeita por um segundo corpo que sustenta so campo opcional — que e "
  "precisamente o mundo que o E14 ja aprovava e que esta regra existe para enxergar",
  troca(VALIDADOR, [
      ('        nucleo = [c for c in obrigatorios if c not in isentos and c in sustentado]',
       '        nucleo = [c for c in sustentado]  # MUTACAO')])),
]


def main():
    print("== mutacoes contra a contagem de corpos por campo (E27) ==")
    falhas = []
    for titulo, porque, aplicar in MUTACOES:
        base = tempfile.mkdtemp(prefix="aqm-campo-mut-")
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

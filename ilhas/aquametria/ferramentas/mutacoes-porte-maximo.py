#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MUTACOES DELIBERADAS CONTRA O PORTAO DO ESCOPO DO PORTE (E24/E25) — Aquametria.

    python3 ferramentas/mutacoes-porte-maximo.py

Cada mutacao afrouxa UMA metade da regra E24 ou E25 em `validar-especies.py`, numa
COPIA da ilha, e roda `ferramentas/testar-validador-especies.py` contra a copia.
A mutacao tem de REPROVAR, com codigo de saida 1 e sem traceback. Mutacao que
passa e o portao nao medindo nada — o defeito que a secao 8 do ARQUIPELAGO.md
persegue desde 10/09/2026, quando tres travas novas da Robometria aprovaram
codigo quebrado.

POR QUE ELE EXISTE SEPARADO DO mutacoes-peixes.py: aquele mede o portao da
PAGINA, contra o HTML servido, e a versao 7 do esquema nao tocou em pagina
nenhuma de proposito (a leitura semanal de 14/10 proibe mexer na superficie
desta ilha antes de 21/10, porque e o que destroi a medicao de CTR em curso).
O que nasceu em 15/10 foi portao de BANCO, e quem o vigia e o
testar-validador-especies.py. Mutacao tem de morder o portao que existe.

A FAMILIA DE TODAS ELAS E UMA SO, e e a que o E24 foi desenhado contra: REGRA
QUE PEDE DUAS COISAS, AFROUXADA PARA PEDIR UMA. Cada metade sozinha aprova um
mundo errado diferente, e as duas juntas nao aprovam nenhum — por isso a mutacao
que tira uma metade e a unica que mostra para que a outra serve.
"""
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VALIDADOR = "ferramentas/validar-especies.py"
PORTAO = "ferramentas/testar-validador-especies.py"


def troca(arquivo, de, para, vezes=1):
    """Substituicao exata, que RECUSA operar se o alvo nao estiver la.

    E a trava contra a mutacao inerte: alvo que nao existe mais nao quebra nada e
    o portao passa por engano — 18 de 20 mutacoes desta ilha viraram inertes de
    uma vez em 11/09/2026, quando a bancada trocou de fonte, e seis morreram de
    novo em 23/09 no mutacoes-escada.py.
    """
    def aplicar(base):
        caminho = os.path.join(base, arquivo)
        texto = open(caminho, encoding="utf-8").read()
        if texto.count(de) != vezes:
            raise SystemExit("MUTACAO INERTE: %r aparece %d vez(es) em %s, esperava %d"
                             % (de, texto.count(de), arquivo, vezes))
        open(caminho, "w", encoding="utf-8").write(texto.replace(de, para, vezes))
    return aplicar


MUTACOES = [
 ("E24 para de exigir o NUMERO na clausula de maximo",
  "a metade que impede a clausula de maximo que fala de outra coisa — sem ela a "
  "lagoa de 'no maximo 30 cm de profundidade' qualifica o porte do peixe",
  troca(VALIDADOR,
        "                    if preenchido(porte) and round(float(porte), 4) not in numeros_no_texto(frase):",
        "                    if False:")),

 ("E24 para de exigir a PALAVRA de maximo na clausula",
  "a outra metade: sem ela qualquer clausula literal que traga o numero sustenta "
  "o campo, e os tres registros que escrevem 'ate' passariam a afirmar maximo",
  troca(VALIDADOR,
        "                    if not any(w in texto for w in PALAVRAS_DE_MAXIMO):",
        "                    if False:")),

 ("E24 aceita clausula de maximo que nenhuma fonte escreveu",
  "sem a conferencia de trecho literal a clausula vira prosa de quem digitou, e a "
  "pagina publicaria o escopo com o nome de uma fonte que nao disse aquilo",
  troca(VALIDADOR,
        "                    if not any(frase in ref for ref in refs):\n"
        "                        erro(\"E24\", rid, \"a frase de porte_e_maximo_registrado nao e trecho literal \"",
        "                    if False:\n"
        "                        erro(\"E24\", rid, \"a frase de porte_e_maximo_registrado nao e trecho literal \"")),

 ("E24 aceita clausula de tamanho comum que nenhuma fonte escreveu",
  "o mesmo afrouxamento um nivel abaixo, e este e o numero que a pagina vai usar "
  "para dizer quanto o peixe tem de verdade",
  troca(VALIDADOR,
        "                        elif not any(fr_comum in ref for ref in refs):",
        "                        elif False:")),

 ("E24 aceita tamanho comum que alcanca o porte maximo",
  "a aritmetica do E18 um andar acima: sem ela a ficha pode publicar que a maioria "
  "dos adultos e maior que o maior individuo ja registrado",
  troca(VALIDADOR,
        "                            if de * EM_CENTIMETRO[unidade] >= float(porte):",
        "                            if False:")),

 ("E24 aceita unidade do comum convertida na digitacao",
  "sem ela o campo pode dizer 'cm' sobre uma clausula escrita em milimetro — e e o "
  "E16 que deixaria de conferir o numero, porque ele o procura no texto da fonte",
  troca(VALIDADOR,
        "                        elif fr_comum and unidade not in sem_acento(fr_comum):",
        "                        elif False:")),

 ("E25 passa a ver so a regua AUSENTE, e nao a regua DIFERENTE",
  "a mutacao mais perigosa das sete, porque ela deixa o aviso de pe: ele continua "
  "saindo no barbo rosado (comum.medida null) e cala no par SL/TL, que e o erro de "
  "leitura que a leva 7 mediu em mais de 20 % para peixe de cauda longa",
  troca(VALIDADOR,
        "                        if medida is None or medida != r.get(\"porte_medida\"):",
        "                        if medida is None:")),

 ("valores_numericos para de descer em objeto dentro de objeto",
  "a regua que nao ALCANCA o mundo novo, em vez de errar nele: sem a recursao o "
  "E16 nao ve os dois numeros do `comum` e da por conferido o unico par do banco "
  "que ninguem conferia antes da versao 7",
  troca(VALIDADOR,
        "            achados.extend(valores_numericos(\"%s.%s\" % (campo, chave), v))",
        "            achados.extend([] if isinstance(v, dict) else "
        "valores_numericos(\"%s.%s\" % (campo, chave), v))")),
]


def main():
    print("== mutacoes contra o portao do escopo do porte (E24/E25) ==")
    falhas = []
    for titulo, porque, aplicar in MUTACOES:
        base = tempfile.mkdtemp(prefix="aqm-porte-mut-")
        copia = os.path.join(base, "ilha")
        shutil.copytree(RAIZ, copia, symlinks=True,
                        ignore=shutil.ignore_patterns("node_modules", ".git", "__pycache__"))
        aplicar(copia)
        # sys.dont_write_bytecode no filho: a mutacao troca poucos caracteres e o
        # .pyc do original pode sobreviver a validacao de mtime + tamanho do
        # Python, que foi o que custou um diagnostico inteiro em 15/10/2026 no
        # portao do search-console.py.
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        r = subprocess.run([sys.executable, os.path.join(copia, PORTAO)],
                           capture_output=True, text=True, cwd=copia, env=env)
        reprovou = r.returncode == 1
        limpo = "Traceback" not in (r.stdout + r.stderr)
        ok = reprovou and limpo
        print("  %-62s %s" % (titulo, "reprovou" if ok else "SOBREVIVEU"))
        if not ok:
            detalhe = "codigo de saida %d" % r.returncode
            if not limpo:
                detalhe += " e traceback (o portao morreu em vez de reprovar)"
            print("      %s" % detalhe)
            print("      para que a metade serve: %s" % porque)
            falhas.append(titulo)
        shutil.rmtree(base, ignore_errors=True)

    print("\n== resultado ==")
    print("  %d mutacao(oes), %d sobrevivente(s)" % (len(MUTACOES), len(falhas)))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MUTACOES DELIBERADAS CONTRA O PORTAO DA REGUA DE CORPOS (16/10/2026).

    python3 ferramentas/mutacoes-regua-de-corpos.py

O mutante e `ferramentas/regua-corpos-de-fonte.py` e os QUATRO portoes que a chamam;
quem tem de reprovar e `ferramentas/teste-regua-de-corpos.py`, com codigo de saida 1,
sem traceback e PELA FRASE CERTA.

POR QUE ELE EXISTE, SEPARADO DO `mutacoes-corpos-de-fonte.py` QUE JA HAVIA
--------------------------------------------------------------------------
Aquele mede a regra E26 pelo validador: a contagem por procedencia e a declaracao
obrigatoria, cobradas por `testar-validador-especies.py`. Ele estava CERTO e continuou
certo — e passava verde com o buraco aberto, porque o buraco nao estava no validador.

Estava nos outros tres consumidores da mesma contagem. Em 15/10/2026 a regra E26 poe a
contagem no esquema e consertou as DUAS reguas que MEDEM o banco; as duas que DECIDEM O
QUE VAI A TELA — `gerar-catalogo-especies.py`, que escreve o snippet que o site serve, e
`teste-peixes.py`, que e o unico portao que compara banco com HTML servido — continuaram
contando corpo pelo PREFIXO DA REFERENCIA. Medido no banco real em 16/10/2026, com a
fonte do usgs-nas (declarada `indeterminada` porque foi oferecida e RECUSADA em 15/10
para este mesmo registro) acrescentada ao `poecilia-reticulata`:

    validador     1 corpo  -> BARRA
    gerador       2 corpos -> PUBLICA
    teste-peixes  2 corpos -> PUBLICA

O validador barrava o guppy e o gerador o punha na tela com UM corpo real, e o unico
portao que olha o HTML servido CONCORDAVA com o gerador. Nada reprovava.

A COBRANCA POR FRASE, que o `mutacoes-segundo-corpo.py` estreou em 16/10/2026 e esta
bateria herda: reprovar nao e a mesma coisa que reprovar PELO MOTIVO CERTO. Sem a
frase, uma mutacao pode disparar outra trava do mesmo portao, voltar vermelha e nunca
ter medido a sua.
"""
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTAO = "ferramentas/teste-regua-de-corpos.py"
REGUA = "ferramentas/regua-corpos-de-fonte.py"
GERADOR = "ferramentas/gerar-catalogo-especies.py"
TESTE_PEIXES = "ferramentas/teste-peixes.py"


def troca(arquivo, pares, vezes=1):
    """Substituicoes exatas que RECUSAM operar se o alvo nao estiver la.

    E a trava contra a mutacao inerte, e ela nao e teorica nesta familia: foi ela que
    parou o `mutacoes-corpos-de-fonte.py` no dia em que a contagem mudou de arquivo, em
    vez de deixar cinco mutacoes passarem por engano sobre um texto que nao existia.
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


# (titulo, frase que a quebra tem de ouvir de volta, para que a trava serve, mutacao)
MUTACOES = [
 ("1. o GERADOR volta a contar corpo pelo prefixo da referencia",
  "fonte indeterminada NAO vira segundo corpo",
  "e a mutacao que E o codigo de 15/10 em pessoa, no portao que escreve o snippet que o "
  "site serve. Com ela, o guppy entra na tela com um corpo real e o validador continua "
  "barrando-o — duas verdades sobre o mesmo registro, e a que vai ao ar e a errada",
  troca(GERADOR, [
      ('    return regua_corpos.corpos_de(especie)',
       '    return {nome_do_corpo(f.get("referencia", "")) or f.get("origem", "")\n'
       '            for f in especie.get("fontes", [])}  # MUTACAO')])),

 ("2. o TESTE-PEIXES volta a contar corpo pelo prefixo da referencia",
  "teste-peixes.py nao redefine a contagem",
  "o portao que compara banco com HTML servido e o UNICO que veria o gerador publicando "
  "errado. Com a regua propria ele concorda com o erro em vez de o acusar, e e por isso "
  "que a metade (B) le os arquivos: comportamento igual no banco de hoje nao prova regua "
  "unica",
  troca(TESTE_PEIXES, [
      ('    if len(regua_corpos.corpos_de(e)) < 2:',
       '    def corpos_de(x):  # MUTACAO\n'
       '        return {corpo_da_referencia(f.get("referencia")) or f.get("origem") or ""\n'
       '                for f in x.get("fontes", [])}\n'
       '    if len(corpos_de(e)) < 2:')])),

 ("3. `indeterminada` passa a contar como corpo proprio, na regua",
  "indeterminada NAO conta",
  "fonte que nao diz de onde veio o numero dela nao e o proprio corpo (nao se sabe se e "
  "dele) nem o de outro (nao se sabe de quem e). Contando, ela promove um registro de "
  "corpo unico a conferido — e foi exatamente este o caso recusado em 15/10",
  troca(REGUA, [
      ('    if corpo["procedencia"] == "indeterminada":\n        return None\n', '')])),

 ("4. `reproduz` conta como si em vez de colapsar, na regua",
  "reproduz colapsa no corpo que reproduz",
  "o reprodutor e o buraco que o hostname nao via: outro corpo, outro dominio, o numero "
  "de um terceiro. Sem o colapso, duas urls servindo o numero do mesmo corpo contam dois",
  troca(REGUA, [('        return corpo.get("reproduz")',
                 '        return corpo["nome"]  # MUTACAO')])),

 ("5. corpo nao declarado volta a contar, pelo host, na regua",
  "host nao declarado nao conta",
  "corpo que ninguem declarou e corpo cuja procedencia ninguem decidiu. Deixa-lo contar "
  "pelo host e voltar ao palpite de que dominio diferente e corpo diferente, que e a "
  "regua que a E26 aposentou",
  troca(REGUA, [
      ('    corpo = corpo_declarado(url)\n    if corpo is None:\n        return None\n',
       '    corpo = corpo_declarado(url)\n    if corpo is None:\n'
       '        return host_da_fonte(url)  # MUTACAO\n')])),

 ("6. o GERADOR deixa de parar diante de corpo nao declarado",
  "corpo nao declarado PARA o gerador",
  "regerar o catalogo com uma fonte cuja procedencia ninguem decidiu publica numero sem "
  "dono. O validador cobra isso pelo E26, e quem rodar o gerador sem o validador nao tem "
  "quem o avise",
  troca(GERADOR, [
      ('            if regua_corpos.corpo_declarado(f.get("url")) is None:\n'
       '                raise SystemExit(',
       '            if False:  # MUTACAO\n'
       '                raise SystemExit(')])),

 ("7. `corpos_por_campo` apaga a chave do campo sem corpo",
  "campo sustentado SO por indeterminada aparece na chave com conjunto vazio",
  "sem a chave vazia, 'campo que nenhum corpo sustenta' e 'campo que ninguem cita' viram "
  "a mesma coisa — e so o primeiro e defeito. E o campo do E27 que tem fonte e nao tem "
  "corpo, que hoje nao tem ocupante e por isso ninguem perceberia",
  troca(REGUA, [('            por_campo.setdefault(campo, set())\n', '')])),

 ("8. `urls_sem_corpo_declarado` devolve lista vazia sempre",
  "host nao declarado e NOMEADO por urls_sem_corpo_declarado",
  "quem reprova precisa NOMEAR a url: 'corpo nao declarado' sem dizer qual manda procurar "
  "em todo o registro. Devolver vazio e a falha silenciosa — a funcao continua existindo "
  "e nunca acusa nada",
  troca(REGUA, [
      ('    return [f.get("url") for f in (registro.get("fontes") or [])',
       '    return []  # MUTACAO\n'
       '    return [f.get("url") for f in (registro.get("fontes") or [])')])),
]


def main():
    print("== mutacoes contra o portao da regua de corpos de fonte ==")
    falhas = []
    for titulo, frase, porque, aplicar in MUTACOES:
        base = tempfile.mkdtemp(prefix="aqm-regua-mut-")
        copia = os.path.join(base, "ilha")
        shutil.copytree(RAIZ, copia, symlinks=True,
                        ignore=shutil.ignore_patterns("node_modules", ".git", "__pycache__"))
        aplicar(copia)
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        r = subprocess.run([sys.executable, os.path.join(copia, PORTAO)],
                           capture_output=True, text=True, cwd=copia, env=env)
        saida = r.stdout + r.stderr
        reprovou = r.returncode == 1
        limpo = "Traceback" not in saida
        # A FRASE: reprovar nao e reprovar pelo motivo certo. A linha da falha comeca por
        # "FALHA ", e e NELA que a frase tem de aparecer — a mesma frase no corpo de um
        # "ok" nao mede nada.
        pela_frase = any(l.strip().startswith("FALHA") and frase in l
                         for l in saida.split("\n"))
        ok = reprovou and limpo and pela_frase
        print("  %-70s %s" % (titulo, "reprovou" if ok else "SOBREVIVEU"))
        if not ok:
            detalhe = "codigo de saida %d" % r.returncode
            if not limpo:
                detalhe += " e traceback (o portao morreu em vez de reprovar)"
            if reprovou and limpo and not pela_frase:
                detalhe += (" — reprovou por OUTRA coisa: nenhuma linha FALHA diz %r"
                            % frase)
            print("      %s" % detalhe)
            print("      para que a trava serve: %s" % porque)
            falhas.append(titulo)
        shutil.rmtree(base, ignore_errors=True)

    print("\n== resultado ==")
    print("  %d mutacao(oes), %d sobrevivente(s), todas cobradas pela frase"
          % (len(MUTACOES), len(falhas)))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

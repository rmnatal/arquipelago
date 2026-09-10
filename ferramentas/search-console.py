#!/usr/bin/env python3
"""
Leitura da Search Console pela nuvem — Projeto Arquipélago.

Uso:
    python3 ferramentas/search-console.py <ilha> [--dias 7] [--json]

    <ilha>  slug da ilha (aquametria, robometria...). A propriedade é
            sempre a de domínio: sc-domain:<ilha>.com.br

Credencial: variável de ambiente GOOGLE_SA_B64 (o JSON da conta de serviço em base64,
uma linha só — é o que a caixa de variáveis do ambiente aceita); alternativas GOOGLE_SA_JSON
(conteúdo cru) ou GOOGLE_SA_FILE (caminho). Nunca no repositório.

Saída (markdown pronto para colar nas séries da ilha):
    1) linha para dados/indexacao.md  (URLs no sitemap × URLs indexadas)
    2) linhas para dados/posicoes.md  (consulta, página, posição, impressões, cliques, banda)

Dependência: google-auth — instalado num venv próprio (~/.venv-search-console) na 1ª execução.
"""
import json, os, sys, datetime as dt, subprocess, urllib.request, urllib.parse, re

def _bootstrap_venv():
    """O Python do ambiente das rotinas tem o pacote `cryptography` do sistema quebrado
    (`_cffi_backend` ausente, pyo3 PanicException). Em vez de depender dele, o script cria
    um venv próprio uma vez (~/.venv-search-console), instala google-auth lá e se re-executa."""
    if os.environ.get("SC_VENV") == "1":
        sys.exit("google-auth não importa nem dentro do venv próprio — ambiente Python inutilizável.")
    venv = os.path.expanduser("~/.venv-search-console")
    py = os.path.join(venv, "bin", "python3")
    if not os.path.exists(py):
        subprocess.check_call([sys.executable, "-m", "venv", venv])
        env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
        for tentativa in range(3):
            if subprocess.call([py, "-m", "pip", "install", "-q", "google-auth", "requests"], env=env) == 0:
                break
        else:
            sys.exit("pip não conseguiu instalar google-auth no venv (3 tentativas).")
    os.environ["SC_VENV"] = "1"
    os.execv(py, [py] + sys.argv)


try:
    from google.oauth2 import service_account
    from google.auth.transport.requests import AuthorizedSession
except BaseException:          # BaseException de propósito: o pyo3 lança PanicException
    _bootstrap_venv()

SCOPE = ["https://www.googleapis.com/auth/webmasters.readonly"]
API = "https://searchconsole.googleapis.com"


def credenciais():
    """Aceita, nesta ordem: GOOGLE_SA_B64 (JSON em base64, uma linha — o formato que a caixa
    de variáveis do ambiente aceita), GOOGLE_SA_JSON (conteúdo cru) ou GOOGLE_SA_FILE (caminho)."""
    import base64
    b64 = os.environ.get("GOOGLE_SA_B64", "").strip().strip("'\"")
    raw = os.environ.get("GOOGLE_SA_JSON", "").strip().strip("'\"")
    path = os.environ.get("GOOGLE_SA_FILE")
    if b64:
        raw = base64.b64decode(b64).decode("utf-8-sig")
    if raw:
        info = json.loads(raw)
        return service_account.Credentials.from_service_account_info(info, scopes=SCOPE)
    if path:
        return service_account.Credentials.from_service_account_file(path, scopes=SCOPE)
    sys.exit("Sem credencial: defina GOOGLE_SA_B64 (base64), GOOGLE_SA_JSON (conteúdo) ou GOOGLE_SA_FILE (caminho).")


def banda(pos, impressoes):
    if impressoes == 0:
        return "sem impressão"
    if pos >= 21:
        return "21+"
    if pos >= 11:
        return "11-20"
    if pos >= 4:
        return "4-10"
    return "1-3"


def urls_do_sitemap(dominio):
    """Lê o sitemap do site (precisa de rede para o domínio; se bloqueado, devolve [])."""
    urls = []
    for candidato in (f"https://{dominio}/wp-sitemap.xml", f"https://{dominio}/sitemap.xml"):
        try:
            xml = urllib.request.urlopen(candidato, timeout=20).read().decode()
        except Exception:
            continue
        subs = re.findall(r"<loc>([^<]+)</loc>", xml)
        for s in subs:
            if s.endswith(".xml"):
                try:
                    x2 = urllib.request.urlopen(s, timeout=20).read().decode()
                    urls += re.findall(r"<loc>([^<]+)</loc>", x2)
                except Exception:
                    pass
            else:
                urls.append(s)
        if urls:
            break
    return sorted(set(urls))


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    ilha = sys.argv[1].strip().lower()
    dias = 7
    if "--dias" in sys.argv:
        dias = int(sys.argv[sys.argv.index("--dias") + 1])
    dominio = f"{ilha}.com.br"
    prop = f"sc-domain:{dominio}"
    sess = AuthorizedSession(credenciais())

    # 0) a conta enxerga a propriedade?
    sites = sess.get(f"{API}/webmasters/v3/sites").json()
    vistos = [s["siteUrl"] for s in sites.get("siteEntry", [])]
    if prop not in vistos:
        sys.exit(f"A conta de serviço não tem acesso a {prop}. Propriedades visíveis: {vistos}")

    hoje = dt.date.today()
    fim = hoje - dt.timedelta(days=2)          # SC atrasa ~2 dias
    ini = fim - dt.timedelta(days=dias - 1)

    # 1) posições por consulta+página
    body = {"startDate": ini.isoformat(), "endDate": fim.isoformat(),
            "dimensions": ["query", "page"], "rowLimit": 500}
    r = sess.post(f"{API}/webmasters/v3/sites/{urllib.parse.quote(prop, safe='')}/searchAnalytics/query",
                  json=body).json()
    linhas = r.get("rows", [])
    impressoes_total = sum(int(x["impressions"]) for x in linhas)
    cliques_total = sum(int(x["clicks"]) for x in linhas)

    # 2) indexação: URL Inspection por URL do sitemap (cota 2000/dia — ok para ilhas pequenas)
    urls = urls_do_sitemap(dominio)
    indexadas, detalhes = 0, []
    for u in urls:
        ins = sess.post(f"{API}/v1/urlInspection/index:inspect",
                        json={"inspectionUrl": u, "siteUrl": prop}).json()
        st = ins.get("inspectionResult", {}).get("indexStatusResult", {})
        verdict, cov = st.get("verdict", "?"), st.get("coverageState", "?")
        ok = verdict == "PASS"
        indexadas += ok
        detalhes.append((u, "indexada" if ok else "NÃO", cov))

    if "--json" in sys.argv:
        print(json.dumps({"ilha": ilha, "propriedade": prop, "periodo": [ini.isoformat(), fim.isoformat()],
                          "urls_sitemap": len(urls), "indexadas": indexadas,
                          "impressoes": impressoes_total, "cliques": cliques_total,
                          "posicoes": linhas, "inspecao": detalhes}, ensure_ascii=False, indent=1))
        return

    pct = f"{100*indexadas/len(urls):.0f}%" if urls else "n/d"
    print(f"## {ilha} — leitura Search Console {hoje.isoformat()} (janela {ini}→{fim})")
    print()
    print("### linha para dados/indexacao.md")
    print(f"| {hoje.isoformat()} | {len(urls) or 'n/d'} | {indexadas if urls else 'n/d'} | {pct} | {impressoes_total} | {cliques_total} |")
    print()
    print("### linhas para dados/posicoes.md")
    print("| consulta | página | posição hoje | impressões | cliques | banda |")
    for x in sorted(linhas, key=lambda z: -int(z["impressions"]))[:60]:
        q, pg = x["keys"]
        pos = float(x["position"])
        pg = pg.replace(f"https://{dominio}", "")
        print(f"| {q} | {pg} | {pos:.1f} | {int(x['impressions'])} | {int(x['clicks'])} | {banda(pos, int(x['impressions']))} |")
    if urls:
        print()
        print("### URLs não indexadas (URL Inspection)")
        for u, st, cov in detalhes:
            if st != "indexada":
                print(f"- {u.replace('https://'+dominio, '')} — {cov}")


if __name__ == "__main__":
    main()

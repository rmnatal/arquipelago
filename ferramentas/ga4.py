#!/usr/bin/env python3
"""
Leitura do GA4 pela nuvem — Projeto Arquipélago.

Uso:
    python3 ferramentas/ga4.py <ilha> [--dias 7] [--json]

    <ilha>  slug da ilha (aquametria, robometria, clubedomosaico).

Credencial: a MESMA da Search Console — GOOGLE_SA_B64 (JSON da conta de serviço em base64,
uma linha só), ou GOOGLE_SA_JSON (conteúdo cru), ou GOOGLE_SA_FILE (caminho). Nunca no repositório.
A conta de serviço é Leitor na conta 'Arquipélago' (407777291) do Analytics, então vale para
toda propriedade dela, inclusive as de ilhas que ainda nem nasceram.

Saída (markdown pronto para as séries da ilha):
    1) linha de totais para dados/audiencia.md
    2) linhas por canal
    3) linhas por origem/mídia, com a coluna IA marcada — é a seção 5 do ARQUIPELAGO.md
       (visibilidade em IA) virando número em vez de opinião.

Dependência: google-auth — mesmo venv da search-console.py (~/.venv-search-console).
"""
import json, os, sys, datetime as dt, subprocess


def _bootstrap_venv():
    """Mesma cicatriz da search-console.py: o Python do ambiente das rotinas tem o
    `cryptography` do sistema quebrado. O script cria/reusa um venv próprio e se re-executa."""
    if os.environ.get("SC_VENV") == "1":
        sys.exit("google-auth não importa nem dentro do venv próprio — ambiente Python inutilizável.")
    venv = os.path.expanduser("~/.venv-search-console")
    py = os.path.join(venv, "bin", "python3")
    if not os.path.exists(py):
        subprocess.check_call([sys.executable, "-m", "venv", venv])
        env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
        for _ in range(3):
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

SCOPE = ["https://www.googleapis.com/auth/analytics.readonly"]
API = "https://analyticsdata.googleapis.com/v1beta"

# Propriedades da conta 'Arquipélago' (407777291). Ilha nova entra aqui no dia em que
# a propriedade nascer — e o ID de medição fica no PROMPT.md da ilha.
PROPRIEDADES = {
    "aquametria":     "553860444",
    "robometria":     "553889920",
    "clubedomosaico": "553922792",
}

# Origens que são assistente de IA. A lista cresce; o que não estiver aqui não é chutado
# como IA — aparece na tabela sem a marca, e quem ler decide.
FONTES_IA = ("chatgpt.com", "perplexity", "gemini.google.com", "claude.ai", "copilot.microsoft.com",
             "bing.com/chat", "you.com", "poe.com", "deepseek")


def credenciais():
    import base64
    b64 = os.environ.get("GOOGLE_SA_B64", "").strip().strip("'\"")
    raw = os.environ.get("GOOGLE_SA_JSON", "").strip().strip("'\"")
    path = os.environ.get("GOOGLE_SA_FILE")
    if b64:
        raw = base64.b64decode(b64).decode("utf-8-sig")
    if raw:
        return service_account.Credentials.from_service_account_info(json.loads(raw), scopes=SCOPE)
    if path:
        return service_account.Credentials.from_service_account_file(path, scopes=SCOPE)
    sys.exit("Sem credencial: defina GOOGLE_SA_B64 (base64), GOOGLE_SA_JSON (conteúdo) ou GOOGLE_SA_FILE (caminho).")


def relatorio(sessao, prop, dimensoes, metricas, dias, limite=25):
    corpo = {
        "dateRanges": [{"startDate": f"{dias}daysAgo", "endDate": "yesterday"}],
        "dimensions": [{"name": d} for d in dimensoes],
        "metrics": [{"name": m} for m in metricas],
        "limit": limite,
    }
    if metricas:
        corpo["orderBys"] = [{"desc": True, "metric": {"metricName": metricas[0]}}]
    r = sessao.post(f"{API}/properties/{prop}:runReport", json=corpo, timeout=60)
    if r.status_code != 200:
        sys.exit(f"GA4 respondeu {r.status_code}: {r.text[:400]}")
    d = r.json()
    linhas = []
    for linha in d.get("rows", []):
        linhas.append(
            [v.get("value", "") for v in linha.get("dimensionValues", [])] +
            [v.get("value", "0") for v in linha.get("metricValues", [])]
        )
    return linhas


def e_ia(origem, midia):
    alvo = f"{origem} {midia}".lower()
    return "ai-assistant" in alvo or any(f in alvo for f in FONTES_IA)


def main():
    args = [a for a in sys.argv[1:]]
    if not args:
        sys.exit("Uso: python3 ferramentas/ga4.py <ilha> [--dias 7] [--json]")
    ilha = args[0]
    dias = 7
    if "--dias" in args:
        dias = int(args[args.index("--dias") + 1])
    saida_json = "--json" in args
    prop = PROPRIEDADES.get(ilha)
    if not prop:
        sys.exit(f"Ilha '{ilha}' não tem propriedade GA4 registrada em PROPRIEDADES. Ilhas conhecidas: "
                 + ", ".join(sorted(PROPRIEDADES)))

    sessao = AuthorizedSession(credenciais())
    hoje = dt.date.today().isoformat()

    totais = relatorio(sessao, prop, [], ["sessions", "activeUsers", "screenPageViews"], dias, 1)
    canais = relatorio(sessao, prop, ["sessionDefaultChannelGroup"], ["sessions"], dias)
    origens = relatorio(sessao, prop, ["sessionSource", "sessionMedium"], ["sessions"], dias)

    s, u, v = (totais[0] if totais else ["0", "0", "0"])
    sessoes_ia = sum(int(o[2]) for o in origens if e_ia(o[0], o[1]))

    if saida_json:
        print(json.dumps({
            "ilha": ilha, "propriedade": prop, "medido_em": hoje, "dias": dias,
            "sessoes": int(s), "usuarios": int(u), "visualizacoes": int(v),
            "sessoes_ia": sessoes_ia,
            "canais": [{"canal": c[0], "sessoes": int(c[1])} for c in canais],
            "origens": [{"origem": o[0], "midia": o[1], "sessoes": int(o[2]), "ia": e_ia(o[0], o[1])} for o in origens],
        }, ensure_ascii=False, indent=2))
        return

    print(f"## {ilha} — GA4, últimos {dias} dias (medido em {hoje}, propriedade {prop})")
    print()
    if int(s) == 0:
        print("**Zero sessão no período.** Isso é dado, não falha: ou a tag ainda não está no ar,")
        print("ou a ilha ainda não recebe visita. Confira o `gtag` no HTML servido antes de concluir.")
        print()
    print(f"| sessões | usuários | visualizações | sessões vindas de IA |")
    print(f"|---|---|---|---|")
    print(f"| {s} | {u} | {v} | {sessoes_ia} |")
    print()
    print("### Por canal")
    print("| canal | sessões |")
    print("|---|---|")
    for c in canais:
        print(f"| {c[0]} | {c[1]} |")
    print()
    print("### Por origem / mídia")
    print("| origem | mídia | sessões | IA |")
    print("|---|---|---|---|")
    for o in origens:
        print(f"| {o[0]} | {o[1]} | {o[2]} | {'sim' if e_ia(o[0], o[1]) else ''} |")


if __name__ == "__main__":
    main()

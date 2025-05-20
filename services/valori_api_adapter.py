def run_simulation(payload: dict):
    kapital = payload["parameter"]["kapital"]
    return {
        "hinweis": "Lokale Demo-Simulation aktiv",
        "etf_nach_steuer": round(kapital * 1.85, 2),
        "immobilie_nach_steuer": round(kapital * 1.65, 2),
        "entscheidung": "ETF bringt mehr – bei höherem Risiko"
    }

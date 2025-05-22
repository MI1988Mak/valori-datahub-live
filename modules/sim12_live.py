from datahub.live_data_router import get_live_value

def run_sim12_with_params(kapital: float, ruecklage_prozent: float, weitergabe_prozent: float, jahre: int) -> dict:
    try:
        rendite_etf = (get_live_value("etf.msci_world.10y_return") or 7.0) / 100
        steuer = get_live_value("steuern.abgeltungssatz") or 0.2625

        # Begrenzung der Aufteilung auf 100 %
        gesamt_prozent = ruecklage_prozent + weitergabe_prozent
        if gesamt_prozent > 100:
            return {
                "sim_id": "sim12",
                "fehler": "Rücklage und Weitergabe übersteigen 100 %",
                "hinweis": "Bitte maximal 100 % des Kapitals aufteilen."
            }

        # Aufteilung
        ruecklage = kapital * (ruecklage_prozent / 100)
        weitergabe = kapital * (weitergabe_prozent / 100)
        investition = kapital - ruecklage - weitergabe

        # Entwicklung
        brutto = investition * ((1 + rendite_etf) ** jahre)
        netto = brutto * (1 - steuer)

        return {
            "sim_id": "sim12",
            "kapital": kapital,
            "jahre": jahre,
            "ruecklage": round(ruecklage, 2),
            "weitergabe": round(weitergabe, 2),
            "investition": round(investition, 2),
            "rendite_etf": round(rendite_etf * 100, 2),
            "steuer": round(steuer, 4),
            "netto_investition": round(netto, 2),
            "revision": "Empfehlung zur Neuaufteilung bei geänderten Lebensumständen oder Prioritäten."
        }

    except Exception as e:
        return {
            "sim_id": "sim12",
            "fehler": str(e),
            "hinweis": "Simulation fehlgeschlagen – bitte Eingaben oder Live-Werte prüfen."
        }

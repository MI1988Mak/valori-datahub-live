from datahub.live_data_router import get_live_value

def run_sim12_with_params(kapital: float, ruecklage_prozent: float, weitergabe_prozent: float, jahre: int) -> dict:
    rendite_etf = (get_live_value("etf.msci_world.10y_return") or 7.0) / 100
    steuer = get_live_value("steuern.abgeltungssatz") or 0.2625

    try:
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
            "auftragsklaerung": "Wie lässt sich eine Erbschaft sinnvoll aufteilen in Rücklage, Investition und Weitergabe?",
            "beispiel": {
                "kapital": kapital,
                "jahre": jahre,
                "ruecklage": round(ruecklage, 2),
                "weitergabe": round(weitergabe, 2),
                "investition": round(investition, 2),
                "real_rendite": round(rendite_etf * 100, 2)
            },
            "ergebnis": f"Aus {round(investition, 2)} Euro werden ca. {round(netto, 2)} Euro nach Steuern.",
            "revision": "Neue Strukturierung sinnvoll bei Lebensveränderungen oder gesetzlichen Änderungen."
        }

    except Exception as e:
        return {
            "sim_id": "sim12",
            "fehler": str(e),
            "hinweis": "Möglicherweise fehlt ein Live-Wert oder Berechnungsfehler bei Aufteilung."
        }

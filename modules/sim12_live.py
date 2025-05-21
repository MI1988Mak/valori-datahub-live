from datahub.live_data_router import get_live_value

def run_sim12_with_params(kapital: float, ruecklage_prozent: float, weitergabe_prozent: float, jahre: int) -> dict:
    rendite_etf = get_live_value("etf.msci_world.10y_return") / 100
    steuer = get_live_value("steuern.abgeltungssatz")

    # Aufteilung des Kapitals
    ruecklage = kapital * (ruecklage_prozent / 100)
    weitergabe = kapital * (weitergabe_prozent / 100)
    investition = kapital - ruecklage - weitergabe

    # Entwicklung der Investition
    brutto = investition * ((1 + rendite_etf) ** jahre)
    netto = brutto * (1 - steuer)

    return {
        "sim_id": "sim12",
        "auftragsklaerung": "Wie lässt sich eine Erbschaft sinnvoll aufteilen in Rücklage, Investition und Weitergabe?",
        "beispiel": {
            "kapital": kapital,
            "jahre": jahre,
            "ruecklage": ruecklage,
            "weitergabe": weitergabe,
            "investition": investition,
            "real_rendite": round(rendite_etf * 100, 2)
        },
        "ergebnis": f"Aus {round(investition, 2)} Euro werden ca. {round(netto, 2)} Euro nach Steuern.",
        "revision": "Neue Strukturierung sinnvoll bei Lebensveränderungen oder gesetzlichen Änderungen."
    }

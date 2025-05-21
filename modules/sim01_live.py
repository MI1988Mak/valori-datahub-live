from datahub.live_data_router import get_live_value

def run_sim01_with_params(kapital: float, jahre: int) -> dict:
    rendite_etf = get_live_value("etf.msci_world.10y_return") / 100
    rendite_immobilie = get_live_value("immobilien.rendite_durchschnitt") / 100
    steuer = get_live_value("steuern.abgeltungssatz")

    # Entwicklung
    brutto_etf = kapital * ((1 + rendite_etf) ** jahre)
    netto_etf = brutto_etf * (1 - steuer)

    brutto_immo = kapital * ((1 + rendite_immobilie) ** jahre)
    netto_immo = brutto_immo * (1 - steuer)

    return {
        "sim_id": "sim01",
        "auftragsklaerung": "Vergleich von ETF und Immobilie als Kapitalanlage über längeren Zeitraum.",
        "beispiel": {
            "kapital": kapital,
            "jahre": jahre,
            "rendite_etf": round(rendite_etf * 100, 2),
            "rendite_immobilie": round(rendite_immobilie * 100, 2),
            "steuer": steuer
        },
        "ergebnis": f"ETF ergibt ca. {round(netto_etf, 2)} €, Immobilie ca. {round(netto_immo, 2)} € nach Steuern.",
        "revision": "Eine Neubewertung ist sinnvoll bei Zinsänderungen, regionalen Immobilienrisiken oder neuen Steuerregeln."
    }

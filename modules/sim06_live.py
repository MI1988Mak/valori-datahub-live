from datahub.live_data_router import get_live_value

def run_sim06_with_params(kapital: float, jahre: int) -> dict:
    # Live-Daten abrufen oder Default verwenden
    inflation = get_live_value("inflation.germany.2025_q2") or 2.5
    rendite_etf = get_live_value("etf.msci_world.10y_return") or 7.0
    steuer = get_live_value("steuern.abgeltungssatz") or 0.2625

    try:
        # Prozentwerte korrekt skalieren
        realrendite = (rendite_etf - inflation) / 100
        brutto = kapital * ((1 + realrendite) ** jahre)
        netto = brutto * (1 - steuer)

        return {
            "sim_id": "sim06",
            "auftragsklaerung": "Was bringt mehr Realertrag bei Inflation – ETF mit langer Laufzeit?",
            "beispiel": {
                "kapital": kapital,
                "jahre": jahre,
                "rendite_etf": rendite_etf,
                "inflation": inflation,
                "realrendite": round(realrendite * 100, 2)
            },
            "ergebnis": f"ETF erzielt nach Steuern und Inflation ca. {round(netto, 2)} Euro Endwert.",
            "revision": "Anpassung sinnvoll bei Inflation > 3 % oder verkürztem Anlagehorizont."
        }
    except Exception as e:
        return {
            "sim_id": "sim06",
            "fehler": str(e),
            "hinweis": "Wahrscheinlich fehlt ein Live-Wert oder ist ungültig."
        }

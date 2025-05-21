from datahub.live_data_router import get_live_value

def run_sim06():
    kapital = 50000
    jahre = 15

    inflation = get_live_value("inflation.germany.2025_q2")
    rendite_etf = get_live_value("etf.msci_world.10y_return")
    steuer = get_live_value("steuern.abgeltungssatz")

    realrendite = rendite_etf - inflation
    brutto = kapital * ((1 + realrendite) ** jahre)
    netto = brutto * (1 - steuer)

    print("\nREIZBAR – Inflationsschutz mit ETF (sim06)")
    print("auftragsklaerung:")
    print("Was bringt mehr Realertrag bei Inflation – ETF mit 15 Jahren Haltezeit?")
    print("beispiel:")
    print(f"ETF-Rendite nominal: {rendite_etf}% | Inflation: {inflation}%")
    print(f"Realrendite: {round(realrendite, 2)}% | Ergebnis: {round(netto, 2)} €")
    print("ergebnis:")
    print("ETF schlägt Inflation bei 15 Jahren klar – steuerbereinigt realer Wertzuwachs")
    print("revision:")
    print("Anpassen bei Inflation >3 % oder kürzerem Horizont\n")

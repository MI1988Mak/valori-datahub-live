def get_immobilienpreise(city="Berlin"):
    benchmark = {
        "Berlin": {"price_per_sqm": 4820, "rendite_erwartet": 0.03},
        "München": {"price_per_sqm": 8100, "rendite_erwartet": 0.025},
        "Hamburg": {"price_per_sqm": 5400, "rendite_erwartet": 0.028}
    }
    return benchmark.get(city, {"price_per_sqm": 5000, "rendite_erwartet": 0.03})

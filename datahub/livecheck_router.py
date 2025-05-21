from fastapi import APIRouter
from datahub.live_data_router import get_live_value

live_router = APIRouter()

live_keys = [
    "etf.msci_world.10y_return",
    "inflation.germany.2025_q2",
    "steuern.abgeltungssatz",
    "immobilien.rendite_durchschnitt"
]

@live_router.get("/valori/livecheck", summary="Live-Daten Diagnose")
def livecheck():
    results = {}
    for key in live_keys:
        value = get_live_value(key)
        results[key] = value if value is not None else "FEHLT"
    return {
        "live_status": results,
        "hinweis": "Werte mit 'FEHLT' sollten in valori_livedata.yaml ergänzt werden."
    }

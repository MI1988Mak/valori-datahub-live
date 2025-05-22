
from fastapi import APIRouter, Query
from modules import etf_api, immo_api
from services import valori_api_adapter
from datahub.live_data_router import get_live_value
from modules.sim06_live import run_sim06_with_params
from modules.sim01_live import run_sim01_with_params

router = APIRouter()

# Ursprünglicher Adapter-basierter sim01-Endpunkt (für externe Datenquellen)
@router.get("/valori/simulation", summary="Simulation über Adapter (ETF vs. Immobilie)")
def run_valori_sim(
    city: str = Query(default="Berlin"),
    etf: str = Query(default="URTH"),
    kapital: float = Query(default=50000)
):
    etf_data = etf_api.get_etf_daten(etf)
    immo_data = immo_api.get_immobilienpreise(city)

    sim_payload = {
        "sim_id": "sim01",
        "parameter": {
            "kapital": kapital,
            "rendite_etf": etf_data["return_10y"] / 100,
            "rendite_immobilie": immo_data["rendite_erwartet"],
            "kostenquote_etf": etf_data["ter"],
            "kostenquote_immobilie": 0.01,
            "steuersatz": 0.2625,
            "laufzeit_jahre": 15
        }
    }

    return valori_api_adapter.run_simulation(sim_payload)

# Neue, direkte und robuste sim01-Testroute (nutzt lokalen Rechenkern mit Fallback)
@router.get("/valori/test-sim01", summary="Direkte Vergleichs-Simulation ETF vs. Immobilie")
def run_sim01_test(
    kapital: float = Query(..., description="Startkapital in Euro"),
    jahre: int = Query(..., description="Laufzeit in Jahren")
):
    return run_sim01_with_params(kapital, jahre)

# Bestehende sim06-Routine: Inflationsschutz (robust)
@router.get("/valori/sim06", summary="Inflationsschutz durch ETF (sim06)")
def run_valori_sim06(
    kapital: float = Query(..., description="Startkapital in Euro"),
    jahre: int = Query(..., description="Laufzeit in Jahren")
):
    return run_sim06_with_params(kapital, jahre)

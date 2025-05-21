from fastapi import FastAPI
from data_router import router
from datahub.livecheck_router import live_router  # <- Livecheck-Router importieren

app = FastAPI(
    title="VALORI DataHub",
    description="Live-Daten + Simulation für kapitalbezogene Entscheidungen",
    version="1.0"
)

# Hauptrouter mit sim01, sim06, sim12 usw.
app.include_router(router)

# Live-Daten-Diagnose-Endpunkt
app.include_router(live_router)

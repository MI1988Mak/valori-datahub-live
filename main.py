from fastapi import FastAPI
from data_router import router
from datahub.livecheck_router import live_router      # Diagnose: Live-Werte prüfen
from datahub.live_update_router import update_router  # Admin: Live-Werte setzen

app = FastAPI(
    title="VALORI DataHub",
    description="Live-Daten + Simulation für kapitalbezogene Entscheidungen",
    version="1.0"
)

# Haupt-Router für sim01, sim06, sim12 usw.
app.include_router(router)

# Diagnose-Endpunkt: /valori/livecheck
app.include_router(live_router)

# Admin-Endpunkt: /valori/liveupdate?auth=valori123
app.include_router(update_router)

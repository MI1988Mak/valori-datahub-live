from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from data_router_perfekt import router as main_router
from datahub.livecheck_router import live_router
from datahub.live_update_router import update_router

app = FastAPI(
    title="VALORI DataHub",
    description="Live-Daten + Simulation für kapitalbezogene Entscheidungen",
    version="1.0"
)

# CORS-Freigabe – erlaubt externe Web-Interfaces wie GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Für produktive Nutzung ggf. auf bestimmte Domains einschränken
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router einbinden
app.include_router(main_router, prefix="/valori", tags=["Simulation"])
app.include_router(live_router, prefix="/valori", tags=["Diagnose"])
app.include_router(update_router, prefix="/valori", tags=["Admin"])

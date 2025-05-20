from fastapi import FastAPI
from data_router import router

app = FastAPI(title="VALORI DataHub", description="Live-Daten + Simulation")
app.include_router(router)

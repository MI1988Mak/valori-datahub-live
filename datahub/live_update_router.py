from fastapi import APIRouter, Request, HTTPException
import yaml
from pathlib import Path

update_router = APIRouter()
YAML_PATH = Path("datahub/valori_livedata.yaml")
AUTH_SECRET = "valori123"  # einfacher Zugangsschutz

def write_live_value(path: str, value, file_path: Path = YAML_PATH):
    if not file_path.exists():
        raise FileNotFoundError("Live-Daten-Datei fehlt.")

    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    keys = path.split(".")
    current = data
    for k in keys[:-1]:
        if k not in current or not isinstance(current[k], dict):
            current[k] = {}
        current = current[k]
    current[keys[-1]] = value

    with open(file_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)

@update_router.post("/valori/liveupdate", summary="Live-Wert aktualisieren")
async def live_update(request: Request):
    auth = request.query_params.get("auth")
    if auth != AUTH_SECRET:
        raise HTTPException(status_code=403, detail="Zugriff verweigert – ungültiges Token")

    body = await request.json()
    key = body.get("key")
    value = body.get("value")

    if not key or value is None:
        raise HTTPException(status_code=400, detail="Key und Value sind erforderlich")

    try:
        write_live_value(key, value)
        return {"status": "OK", "hinweis": f"Wert '{key}' wurde auf '{value}' gesetzt"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fehler beim Schreiben: {str(e)}")

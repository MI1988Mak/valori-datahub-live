import requests

def run_simulation(payload: dict):
    url = "https://api.valori.local/v1/run-simulation"  # ggf. anpassen
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e), "payload": payload}

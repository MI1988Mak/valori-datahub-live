import requests

def run_simulation(payload: dict):
    url = "https://valori-sim-api.onrender.com/v1/run-simulation"
    try:
        response = requests.post(url, json=payload, timeout=10)
        return response.json()
    except Exception as e:
        return {
            "error": str(e),
            "payload": payload
        }

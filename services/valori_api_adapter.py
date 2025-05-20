import requests

def run_simulation(payload: dict):
    url = "https://valori-sim.onrender.com/v1/run-simulation"
    try:
        response = requests.post(url, json=payload, timeout=10)
        return {
            "status_code": response.status_code,
            "raw": response.text,
            "parsed": response.json()
        }
    except Exception as e:
        return {
            "error": str(e),
            "payload": payload
        }

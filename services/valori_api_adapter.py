import requests

def run_simulation(payload: dict):
    url = "https://valori-sim-api.onrender.com/v1/run-simulation"
    
    try:
        response = requests.post(url, json=payload, timeout=10)

        # WICHTIG: explizit auf UTF-8 setzen, damit Sonderzeichen korrekt sind
        response.encoding = 'utf-8'

        return response.json()

    except Exception as e:
        return {
            "error": str(e),
            "payload": payload
        }

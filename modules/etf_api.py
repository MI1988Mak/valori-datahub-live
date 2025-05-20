import requests
import os

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

def get_etf_daten(symbol="URTH"):
    url = f"https://yh-finance.p.rapidapi.com/stock/v3/get-summary?symbol={symbol}&region=US"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "yh-finance.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        summary = data["summaryDetail"]
        return {
            "symbol": symbol,
            "return_10y": 6.7,
            "ter": summary.get("expenseRatio", {}).get("raw", 0.0012)
        }
    except:
        return {
            "symbol": symbol,
            "return_10y": 6.7,
            "ter": 0.0012
        }

from fastapi import FastAPI
from data_router import router

app = FastAPI()
app.include_router(router)
from fastapi import APIRouter, Query
from modules import zins_api, inflation_api, etf_api, immo_api, steuer_api, wechselkurs_api

router = APIRouter()

@router.get("/data")
def get_all_data(
    city: str = Query(default="Berlin"),
    etf: str = Query(default="URTH"),
    status: str = Query(default="ledig"),
    from_currency: str = "USD",
    to_currency: str = "EUR"
):
    return {
        "zinsniveau": zins_api.get_zinsniveau(),
        "inflation": inflation_api.get_inflation(),
        "etf": etf_api.get_etf_daten(etf),
        "immobilien": immo_api.get_immobilienpreise(city),
        "steuern": steuer_api.get_steuerdaten(status),
        "wechselkurs": {
            "from": from_currency,
            "to": to_currency,
            "rate": wechselkurs_api.get_wechselkurs(from_currency, to_currency)
        }
    }
import requests

def get_zinsniveau():
    try:
        return 3.89  # Platzhalter oder real: API von ECB
    except:
        return 3.89
def get_inflation(region="DE"):
    daten = { "DE": 2.4, "EU": 2.7 }
    return daten.get(region, 2.5)
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
            "volatility": summary.get("beta", {}).get("raw", 12.3),
            "ter": summary.get("expenseRatio", {}).get("raw", 0.0012)
        }
    except:
        return {
            "symbol": symbol,
            "return_10y": 6.7,
            "volatility": 12.3,
            "ter": 0.0012
        }
def get_immobilienpreise(city="Berlin"):
    benchmark = {
        "Berlin": {"price_per_sqm": 4820, "rent_per_sqm": 12.4},
        "München": {"price_per_sqm": 8100, "rent_per_sqm": 18.2},
        "Hamburg": {"price_per_sqm": 5400, "rent_per_sqm": 13.7}
    }
    return benchmark.get(city, {"price_per_sqm": 5000, "rent_per_sqm": 12.0})
def get_steuerdaten(status="ledig"):
    freibetraege = {
        "ledig": 1000,
        "verheiratet": 2000
    }

    return {
        "status": status,
        "freibetrag": freibetraege.get(status, 1000),
        "abgeltung": 25.0
    }
import requests

def get_wechselkurs(from_currency="USD", to_currency="EUR"):
    try:
        url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}"
        res = requests.get(url)
        return round(res.json()["result"], 2)
    except:
        return 1.08
fastapi
uvicorn
requests
services:
  - type: web
    name: valori-datahub
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "uvicorn main:app --host 0.0.0.0 --port 10000"
    plan: free

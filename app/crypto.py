


print("CRYPTO REPORT...")

import os
import json
from dotenv import load_dotenv
import requests

from app.utils import to_usd
from app.alphavantage_service import fetch_crypto_data

symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"
dates = list(fetch_crypto_data(symbol).keys())
latest_date = dates[0]
latest = fetch_crypto_data(symbol)[latest_date]

print(symbol)
print(latest_date)
print(latest['4a. close (USD)'])
print(to_usd(float(latest['4a. close (USD)'])))

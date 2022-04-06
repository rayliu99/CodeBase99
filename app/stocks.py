

print("STOCKS REPORT...")

import os
from dotenv import load_dotenv
from pandas import read_csv
from app.utils import to_usd
from app.alphavantage_service import fetch_stocks_data

symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"

#print(df.columns)
#breakpoint()

#print(df.columns)
#breakpoint()

latest = fetch_stocks_data(symbol)

print(symbol)
print(latest["timestamp"])
print(latest["close"])
print(to_usd(latest["close"]))

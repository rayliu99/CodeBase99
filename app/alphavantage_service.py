# maybe something like the following rough organizational structure would be reasonable.
# then we can import these functions into other files that need them (i.e. crypto.py, stocks.py, unemployment.py).
# one benefit of doing so is we get to refactor all the request-related code out of those files.
# for example, as a result, we'll only have the api key definition in one place (which is good)!

import os
from dotenv import load_dotenv
import requests
import json
from pandas import read_csv

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")



def fetch_crypto_data(symbol):
   

    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    #print(parsed_response)
    #breakpoint()

    tsd = parsed_response["Time Series (Digital Currency Daily)"]

    return tsd


def fetch_stocks_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"

    df = read_csv(url)
    #print(df.columns)
    #breakpoint()

    latest = df.iloc[0]
    return latest


def fetch_unemployment_data():
    # docs: https://www.alphavantage.co/documentation/#unemployment
    url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    data = parsed_response["data"]
    #print(parsed_response) 
    return data
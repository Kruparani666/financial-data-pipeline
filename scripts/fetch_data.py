import requests
import pandas as pd

API_KEY = "********"   # Replace with your API key
SYMBOL = "AAPL"

URL = "https://www.alphavantage.co/query"
PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": SYMBOL,
    "apikey": API_KEY
}

def fetch_stock_data():
    response = requests.get(URL, params=PARAMS)
    data = response.json()

    time_series = data["Time Series (Daily)"]
    df = pd.DataFrame.from_dict(time_series, orient="index")

    df.to_csv(f"data/{SYMBOL}_raw_data.csv")
    print("✅ Raw data saved")

if __name__ == "__main__":
    fetch_stock_data()

import pandas as pd

SYMBOL = "AAPL"

def process_data():
    df = pd.read_csv(f"data/{SYMBOL}_raw_data.csv", index_col=0)

    df.index = pd.to_datetime(df.index)
    df = df.astype(float)
    df.sort_index(inplace=True)

    df.rename(columns={
        "1. open": "Open",
        "2. high": "High",
        "3. low": "Low",
        "4. close": "Close",
        "5. volume": "Volume"
    }, inplace=True)

    # Feature engineering
    df["Daily_Return"] = df["Close"].pct_change()
    df["MA_20"] = df["Close"].rolling(window=20).mean()
    df["MA_50"] = df["Close"].rolling(window=50).mean()

    df.dropna(inplace=True)
    df.to_csv(f"data/{SYMBOL}_stock_data.csv")

    print("✅ Processed data saved")

if __name__ == "__main__":
    process_data()

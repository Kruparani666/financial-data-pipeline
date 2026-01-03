import pandas as pd
import matplotlib.pyplot as plt

SYMBOL = "AAPL"

df = pd.read_csv(f"data/{SYMBOL}_stock_data.csv", index_col=0)
df.index = pd.to_datetime(df.index)

plt.figure()
plt.plot(df["Close"], label="Close Price")
plt.plot(df["MA_20"], label="20-Day MA")
plt.plot(df["MA_50"], label="50-Day MA")
plt.title(f"{SYMBOL} Stock Price Analysis")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

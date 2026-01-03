import streamlit as st
import pandas as pd

st.set_page_config(page_title="Stock Dashboard", layout="wide")

SYMBOL = st.text_input("Enter Stock Symbol", "AAPL")

df = pd.read_csv(f"data/{SYMBOL}_stock_data.csv", index_col=0)
df.index = pd.to_datetime(df.index)

st.title("📊 Financial Stock Market Dashboard")

st.subheader("Closing Price")
st.line_chart(df["Close"])

st.subheader("Volume")
st.bar_chart(df["Volume"])

st.subheader("Moving Averages")
st.line_chart(df[["MA_20", "MA_50"]])

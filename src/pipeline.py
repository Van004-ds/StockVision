import streamlit as st
import yfinance as yf
import pandas as pd


@st.cache_data
def load_stock_data(ticker, period="2y"):

    stock = yf.Ticker(ticker)

    df = stock.history(period=period)

    if df.empty:
        raise ValueError("No data found.")

    df.reset_index(inplace=True)

    return df
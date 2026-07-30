import pandas as pd
import numpy as np


def add_features(df):

    # Daily Returns
    df["Returns"] = df["Close"].pct_change()

    # Cumulative Returns
    df["Cumulative_Returns"] = (1 + df["Returns"]).cumprod() - 1

    # Moving Averages
    df["MA_20"] = df["Close"].rolling(window=20).mean()
    df["MA_50"] = df["Close"].rolling(window=50).mean()

    # Rolling Volatility
    df["rolling_volatility"] = (
        df["Returns"].rolling(window=20).std() * np.sqrt(252)
    )

    # Drawdown
    running_max = df["Close"].cummax()
    df["drawdown"] = (df["Close"] - running_max) / running_max

    # RSI (14-day)
    delta = df["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss

    df["RSI"] = 100 - (100 / (1 + rs))

    return df
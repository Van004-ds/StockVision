import pandas as pd


def generate_eda(df):
    """
    Generate summary statistics for the stock dataset.
    """

    summary = {
        "Trading Days": len(df),
        "Start Date": df["Date"].min().date(),
        "End Date": df["Date"].max().date(),
        "Highest Close": round(df["Close"].max(), 2),
        "Lowest Close": round(df["Close"].min(), 2),
        "Average Close": round(df["Close"].mean(), 2),
        "Average Volume": int(df["Volume"].mean()),
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum())
    }

    return summary
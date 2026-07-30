import pandas as pd


def clean_data(df):
    """
    Clean and validate stock data.
    """

    # Create a copy so original data isn't modified
    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    # Sort by Date
    df = df.sort_values("Date")

    # Reset index
    df = df.reset_index(drop=True)

    # Remove rows where Close price is missing
    df = df.dropna(subset=["Close"])

    return df
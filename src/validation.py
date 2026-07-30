import pandas as pd


def validate_data(df):
    """
    Validate downloaded stock data.
    """

    if df.empty:
        raise ValueError("No stock data found.")

    required_columns = [
        "Date",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    if len(df) < 50:
        raise ValueError(
            "Not enough historical data."
        )

    return df
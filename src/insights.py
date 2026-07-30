def generate_insights(df):

    latest = df.iloc[-1]

    insights = {}

    # Trend
    insights["Trend"] = (
        "🟢 Bullish"
        if latest["Close"] > latest["MA_50"]
        else "🔴 Bearish"
    )

    # RSI
    if latest["RSI"] > 70:
        insights["RSI"] = "🔴 Overbought"
    elif latest["RSI"] < 30:
        insights["RSI"] = "🟢 Oversold"
    else:
        insights["RSI"] = "🟡 Neutral"

    # Risk
    if latest["rolling_volatility"] > 0.40:
        insights["Risk"] = "🔴 High"
    elif latest["rolling_volatility"] > 0.20:
        insights["Risk"] = "🟡 Moderate"
    else:
        insights["Risk"] = "🟢 Low"

    # Drawdown
    if latest["drawdown"] < -0.20:
        insights["Drawdown"] = "🔴 Large Drawdown"
    elif latest["drawdown"] < -0.10:
        insights["Drawdown"] = "🟡 Moderate Drawdown"
    else:
        insights["Drawdown"] = "🟢 Healthy"

    

    return insights
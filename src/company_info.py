import yfinance as yf


def format_market_cap(value):
    if value is None:
        return "N/A"

    if value >= 1_000_000_000_000:
        return f"{value/1_000_000_000_000:.2f}T"

    if value >= 1_000_000_000:
        return f"{value/1_000_000_000:.2f}B"

    if value >= 1_000_000:
        return f"{value/1_000_000:.2f}M"

    return str(value)


def get_company_info(selected_stock):

    stock = yf.Ticker(selected_stock)

    # info = stock.info
    info = stock.get_info()
    dividend = info.get("dividendYield")

    if dividend is None:
      dividend = "N/A"
    else:
      dividend = f"{dividend:.2f}%"

    return {

        "Name": info.get("longName", "N/A"),

        "Sector": info.get("sector", "N/A"),

        "Industry": info.get("industry", "N/A"),

        "Exchange": info.get("exchange", "N/A"),

        "Currency": info.get("currency", "N/A"),

        "Market Cap": format_market_cap(info.get("marketCap")),

        "52 Week High": info.get("fiftyTwoWeekHigh", "N/A"),

        "52 Week Low": info.get("fiftyTwoWeekLow", "N/A"),

        "Dividend Yield": dividend,

       

    }
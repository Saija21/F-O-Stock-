import yfinance as yf
import pandas as pd
import datetime

def fetch_intraday_data(symbol):
    ticker = yf.Ticker(symbol + ".NS")
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    df = ticker.history(start=today, end=today)
    if not df.empty:
        return {
            "Symbol": symbol,
            "Open": df["Open"].iloc[0],
            "Close": df["Close"].iloc[0]
        }
    else:
        return None

def main():
    fo_df = pd.read_csv("fo_stock_list.csv")
    fo_symbols = fo_df['Symbol'].tolist()

    results = []
    for symbol in fo_symbols:
        data = fetch_intraday_data(symbol)
        if data and data["Open"] != 0:  # Avoid division by zero
            change_pct = (data["Close"] - data["Open"]) / data["Open"] * 100
            results.append({"Symbol": symbol, "ChangePct": change_pct})

    top_gainers = sorted(results, key=lambda x: x["ChangePct"], reverse=True)[:5]

    print("Top 5 Intraday Gainers:")
    for stock in top_gainers:
        print(f"{stock['Symbol']}: {stock['ChangePct']:.2f}%")
    if name == "main":
    main()
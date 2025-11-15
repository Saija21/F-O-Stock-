import requests
import pandas as pd

def get_fo_stock_list():
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.5"
    }
    session = requests.Session()
    session.get("https://www.nseindia.com", headers=headers)
    response = session.get(url, headers=headers)
    data = response.json()

    symbols = []
    for entry in data["records"]["underlying"]:
        symbols.append(entry)

    
    df = pd.DataFrame(symbols, columns=['Symbol'])
    df.to_csv("fo_stock_list.csv", index=False)
    print(f"Saved {len(symbols)} F&O symbols to fo_stock_list.csv")
    if name == "main":
    get_fo_stock_list()
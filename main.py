import requests
import pandas as pd
import warnings
import datetime as dt
import time


def kline(symb, tf, start):

    url = "https://api.bybit.com"
    path = "/v5/market/kline"
    URL = url + path
    start_ds = dt.datetime.strptime(start, '%Y-%m-%d %H:%M')
    start_ds = int(start_ds.timestamp()*1000)
    end_ds = int(time.time()*1000)

    batch_size = 200
    dtf = int(tf) * 60 * 1000
    N = round(((end_ds - start_ds)/dtf) + 0.5)
    batch_count = N // batch_size + int(N % batch_size != 0)

    dfs = pd.DataFrame()
    for i in range(batch_count):
        batch_start = start_ds + i * batch_size*dtf
        batch_end = min(end_ds, batch_start + batch_size*dtf)
        params = {'category': 'linear', "symbol": symb, "interval": tf, 'start': batch_start, 'end': batch_end}
        r = requests.get(URL, params=params)
        df = pd.DataFrame(r.json()['result']['list'])
        m = pd.DataFrame()
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=FutureWarning)
            m['Date'] = pd.to_datetime(df.iloc[:, 0], unit="ms")
            m['Open'] = df.iloc[:, 1].astype(float)
            m['High'] = df.iloc[:, 2].astype(float)
            m['Low'] = df.iloc[:, 3].astype(float)
            m['Close'] = df.iloc[:, 4].astype(float)
            m['Volume'] = df.iloc[:, 5].astype(float)
            m = m.sort_values(by='Date', ignore_index=True)

        dfs = pd.concat([dfs, m])
    return dfs


if __name__ == "__main__":
    try:
        df = kline("BTCUSDT", 60, "2023-09-09 00:00")
        if df is not None:
            df.to_csv('btc_klines_60m.csv', index=False, encoding='utf-8')
            print(df.head())
        else:
            print("Failed to fetch data. Check console output for details.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
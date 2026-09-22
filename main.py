from datetime import datetime
import pandas as pd
import requests

# 填入你的 Fugle Developer API Key
API_KEY = "NWU1MmE4NGUtNWFjMS00M2YxLThmY2EtYzczZmQyNzRiNjIyIDllMzVlNWM2LWNjODUtNDliNy1hZWU3LThkYjAyODdlMjE0ZQ==EY"
SYMBOL = "2330"  # 以台積電為例


def fetch_fugle_quote(symbol, api_key):
  url = f"https://api.fugle.tw/marketdata/v1.0/stock/intraday/quote/{symbol}"
  headers = {"X-API-KEY": api_key}
  try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
      return response.json()
    else:
      print(f"API 錯誤代碼: {response.status_code}, 內容: {response.text}")
      return None
  except Exception as e:
    print(f"連線異常: {e}")
    return None


def main():
  print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 正在取得 {SYMBOL} 行情...")
  data = fetch_fugle_quote(SYMBOL, API_KEY)

  if not data:
    return

  name = data.get("name", "未知")
  price = data.get("closePrice") or data.get("lastPrice")
  high = data.get("highPrice")
  low = data.get("lowPrice")
  volume = data.get("total", {}).get("tradeVolume")

  print(f"股票：{name} ({SYMBOL})")
  print(f"即時成交價：{price}")
  print(f"最高：{high} | 最低：{low} | 總成交量：{volume}")


if __name__ == "__main__":
  main()

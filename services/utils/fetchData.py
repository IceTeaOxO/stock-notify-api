import pandas as pd
import time
from dotenv import load_dotenv
import os
from fugle_marketdata import WebSocketClient, RestClient
import json
import requests

stock_list_file_name = "./main/model/stock_list.json"
# 加载.env文件中的环境变量
load_dotenv()
    # 读取环境变量的值
api_key = os.getenv('api_key')
client = RestClient(api_key = api_key)
stock = client.stock  # Stock REST API client

with open("./main/model/stock_list.json", "r") as f:
    stock_symbols = json.load(f)

# 策略參數
short_ma_period = 5  # 短期均線週期
long_ma_period = 20  # 長期均線週期

for symbol in stock_symbols:
    # 取得歷史數據
    historical_data = stock.historical.candles(
        symbol=symbol,
        params={
            "from":"2024-04-01",  # 調整起始日期
            "to":"2024-5-06",  # 調整結束日期
            "timeframe":"10"
        }
    )
    print(historical_data)

    # # 計算均線
    # historical_data["short_ma"] = historical_data["close"].rolling(window=short_ma_period).mean()
    # historical_data["long_ma"] = historical_data["close"].rolling(window=long_ma_period).mean()

    # # 應用均線交易策略
    # if historical_data["short_ma"].iloc[-1] > historical_data["long_ma"].iloc[-1] and \
    #    historical_data["short_ma"].iloc[-2] < historical_data["long_ma"].iloc[-2]:
    #     print(f"股票代號: {symbol} 短期均線向上穿越長期均線，買入訊號！")
    #     # ... (執行買入操作等) ...
    # elif historical_data["short_ma"].iloc[-1] < historical_data["long_ma"].iloc[-1] and \
    #      historical_data["short_ma"].iloc[-2] > historical_data["long_ma"].iloc[-2]:
    #     print(f"股票代號: {symbol} 短期均線向下穿越長期均線，賣出訊號！")
    #     # ... (執行賣出操作等) ...
    # else:
    #     print(f"股票代號: {symbol} 沒有交易訊號。")

    # print("-" * 20)
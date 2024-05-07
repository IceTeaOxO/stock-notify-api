import pandas as pd
import time
from dotenv import load_dotenv
import os
from fugle_marketdata import WebSocketClient, RestClient
import json
import requests

# def test(*args, **kwargs):
#     print("Hello World!")
#     time.sleep(5)

def momentum_strategy(**kwargs):
    # 加载.env文件中的环境变量
    load_dotenv()
    # 读取环境变量的值
    api_key = os.getenv('api_key')
    client = RestClient(api_key = api_key)
    stock = client.stock  # Stock REST API client

    # 儲存前一次的股票資訊
    previous_quotes = kwargs.get("previous_quotes", {})



    stock_symbols = kwargs.get("data", [])
    webhook_url = kwargs.get("webhook_url")

    # try:
    #     webhook_time = float(kwargs.get("webhook_time",300))
    # except ValueError:
    #     webhook_time = 300
    
    try:
        min_volume_change_percent = float(kwargs.get("min_volume_change_percent", 3))
    except ValueError:
        min_volume_change_percent = 3
    
    try:
        min_price_change_percent = float(kwargs.get("min_price_change_percent", 1))
    except ValueError:
        min_price_change_percent = 1

    

        # 讀取股票代碼清單
        
    for symbol in stock_symbols:
        # 取得即時報價
        quote = stock.intraday.quote(symbol=symbol)
    
        # 檢查是否有前一次的報價數據
        if symbol in previous_quotes:
            previous_quote = previous_quotes[symbol]


            # 計算五分鐘成交量變化和價格變化
            # volume_change = quote["total"]["tradeVolume"] - previous_quote["total"]["tradeVolume"]
            # price_change = quote["closePrice"] - previous_quote["closePrice"]
            # 計算五分鐘成交量變化百分比和價格變化百分比
            volume_change_percent = (quote["total"]["tradeVolume"] - previous_quote["total"]["tradeVolume"]) / previous_quote["total"]["tradeVolume"] * 100
            price_change_percent = (quote["closePrice"] - previous_quote["closePrice"]) / previous_quote["closePrice"] * 100

            # 應用 Momentum 策略邏輯
            if volume_change_percent > min_volume_change_percent and price_change_percent > min_price_change_percent:
                print(f"股票代號: {symbol} 上漲動力強！")

                response = requests.post(webhook_url, json={"content": f"股票代號: {symbol} 上漲動力強！"})
                # 檢查是否成功
                if response.status_code == 204:
                    print("訊息已成功傳送！")
                else:
                    print(f"訊息傳送失敗：{response.status_code}")
                # ... (執行買入操作等) ...
                
            elif volume_change_percent < -min_volume_change_percent and price_change_percent < -min_price_change_percent:
                print(f"股票代號: {symbol} 下跌動力強！")

                response = requests.post(webhook_url, json={"content": f"股票代號: {symbol} 下跌動力強！"})
                # 檢查是否成功
                if response.status_code == 204:
                    print("訊息已成功傳送！")
                else:
                    print(f"訊息傳送失敗：{response.status_code}")
            else:
                # print(f"股票代號: {symbol} 不符合 Momentum 策略。")
                pass
        else:
            print(f"股票代號: {symbol} 沒有前一次的報價數據。")

        # 更新前一次的報價數據
        previous_quotes[symbol] = quote

    return previous_quotes
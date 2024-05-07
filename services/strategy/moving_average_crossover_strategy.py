# import yfinance as yf
# import pandas as pd
# import numpy as np
# import time

# import yfinance as yf
# import pandas as pd
# import numpy as np
# import time

# def fetch_stock_data(symbol):
#     """
#     獲取股票的實時數據。
#     :param symbol: 股票代碼
#     :return: 包含實時價格的DataFrame
#     """
#     stock = yf.Ticker(symbol)
#     # 獲取最近60天的日線數據用於計算移動平均線
#     hist = stock.history(period='60d', interval='1d')
#     return hist

# def moving_average_crossover_strategy(data, short_window=10, long_window=30):
#     """
#     移動平均線交叉策略。
#     :param data: 包含股票價格的DataFrame
#     :param short_window: 短期移動平均線的窗口大小
#     :param long_window: 長期移動平均線的窗口大小
#     :return: 交叉信號
#     """
#     signals = pd.DataFrame(index=data.index)
#     signals['signal'] = 0.0
    
#     # 計算短期和長期移動平均線
#     signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
#     signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    
#     # 創建信號
#     signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)   
    
#     # 生成交易指令
#     signals['positions'] = signals['signal'].diff()

#     return signals

# def check_for_crossover(symbol):
#     """
#     檢查並打印是否出現移動平均線交叉。
#     :param symbol: 股票代碼
#     """
#     data = fetch_stock_data(symbol)
#     signals = moving_average_crossover_strategy(data)
#     latest_signal = signals['positions'].iloc[-1]
#     if latest_signal > 0:
#         print(f"{symbol}: 黃金交叉發生，建議買入。")
#     elif latest_signal < 0:
#         print(f"{symbol}: 死亡交叉發生，建議賣出。")
#     else:
#         print(f"{symbol}: 無交叉發生。")

# # 主循環，每五分鐘運行一次
# symbol = 'AAPL'
# while True:
#     check_for_crossover(symbol)
#     time.sleep(5)  # 暫停300秒（5分鐘）


# # def fetch_stock_data(symbol, period='1y', interval='1d'):
# #     """
# #     獲取股票數據。
# #     :param symbol: 股票代碼
# #     :param period: 數據期限
# #     :param interval: 數據間隔
# #     :return: DataFrame
# #     """
# #     stock = yf.Ticker(symbol)
# #     hist = stock.history(period=period, interval=interval)
# #     return hist

# # def moving_average_crossover_strategy(data, short_window=10, long_window=30):
# #     """
# #     移動平均線交叉策略。
# #     :param data: 包含股票價格的DataFrame
# #     :param short_window: 短期移動平均線的窗口大小
# #     :param long_window: 長期移動平均線的窗口大小
# #     :return: 交叉信號
# #     """
# #     signals = pd.DataFrame(index=data.index)
# #     signals['signal'] = 0.0
    
# #     # 計算短期和長期移動平均線
# #     signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
# #     signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    
# #     # 創建信號
# #     signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)   
    
# #     # 生成交易指令
# #     signals['positions'] = signals['signal'].diff()

# #     return signals

# # # 使用範例
# # symbol = 'AAPL'
# # data = fetch_stock_data(symbol)
# # signals = moving_average_crossover_strategy(data)

# # # 打印最新的信號
# # print(signals.tail())

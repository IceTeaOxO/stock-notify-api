# 專案動機
因為花太多時間在看股票了，想建立一個系統可以自動通知符合買賣策略的股票
考量到後續會接上網頁或Discord bot，所以只做後端API的部分。

# 使用說明
- 安裝環境
```
pip install -r requirements.txt
```

```
uvicorn main:app --reload
```
# 專案說明
`main.py`是專案進入點
`/model`負責存放設定文件等檔案，以及規定資料的格式
`/services`存放撰寫的service

可以透過API取得當前可用的策略以及股票代號（若有新增策略需要更新文件）
使用該服務前需要按照指定格式傳送requests，server會創建對應的設定文件並開啟線程運行策略，並將符合策略的通知發送到webhook_url中。


- 該專案使用富果行情API取得股票資訊，使用者需要自己去申請API才能夠正常使用
- 記得將`local.env`改名為`env`



## Swagger doc
`http://127.0.0.1:8000/docs`


## Tips
現在有的策略清單`model/strategies.json`
目前只有最簡單的動力策略，未來可能會更新（？
歡迎大家貢獻自己的策略!
```
{
    "strategies": [
        {
            "file_name": "3",
            "strategy": {
            "strategy_name": "momentum_strategy",
            "parameters": {
              "min_volume_change_percent": 3,
              "min_price_change_percent": 1
            }
          },
          "data": [
            "2330","0050"
          ],
          "webhook_url": "https://discord.com/api/webhooks/your_webhook_id/your_webhook_token",
          "webhook_time": "300"
        }
    ]
}
```

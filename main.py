from fastapi import FastAPI, Body
from pydantic import BaseModel
from model.dataModel import RunRequest, TerminateRequest, SettingRequest
import json
import threading
import time
from dotenv import load_dotenv
import os
from services.file.fileManager import FileManager
from fastapi import HTTPException
from services.thread.threadManager import ThreadManager


app = FastAPI()

# 執行策略 API
@app.post("/api/run")
async def run_strategy(request: RunRequest):#
    # 根據使用者的請求，調用線程的service方法，並配置線程的參數
    file_manager = FileManager()
    try:
        file_manager.write_json_to_file(request.model_dump(), request.file_name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    thread_manager = ThreadManager()
    thread_manager.start_thread(request.model_dump())

    return request


# 終止策略 API
@app.post("/api/terminate")
async def terminate_strategy(request: TerminateRequest):
    # 這邊會調用service的方法，更改特定線程的狀態，進而終止線程
    thread_manager = ThreadManager()
    thread_manager.stop_thread_by_name(request.file_name)
    return request

# 在這個專案中，線程健康檢查是直接寫在線程中的，客戶只能透過post的方式取得該線程的狀態

@app.get("/api/threadList")
async def get_thread_list():
    # 取得所有線程的名稱
    thread_manager = ThreadManager()
    thread_names = thread_manager.get_thread_names()
    return thread_names

@app.get("/api/setting/{file_name}")
async def get_setting(file_name: str):
    # 取得特定名稱的json檔案內容
    file_manager = FileManager()
    try:
        file_content = file_manager.read_json_file(file_name)
        print(file_content)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return file_content

@app.post("/api/setting")
async def post_setting(request: SettingRequest):
    # 將資料寫入特定名稱的json檔案
    print(request.model_dump())
    file_manager = FileManager()
    try:
        file_manager.write_json_to_file(request.model_dump(), request.file_name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return {"message": "success"}


# 取得策略列表 API
@app.get("/api/strategy_list")
async def get_strategy_list():
    # 這邊會使用service的方法取得現有的策略列表
    load_dotenv()
    strategy_list_file_name = os.getenv('strategy_list_file_name')
    with open(strategy_list_file_name, "r") as f:
        strategy_list = json.load(f)
    return strategy_list

# 取得股票代號列表 API
@app.get("/api/stock_symbol_list")
async def get_stock_symbol_list():
    # 這邊會使用service的方法取得特定市場的股票代號清單
    load_dotenv()
    stock_list_file_name = os.getenv('stock_list_file_name')

    with open(stock_list_file_name, "r") as f:
        stock_symbols_list = json.load(f)
    return stock_symbols_list


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
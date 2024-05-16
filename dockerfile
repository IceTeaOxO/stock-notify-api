# 使用官方 Python 鏡像作為基礎映像
FROM python:3.11

# 設置工作目錄
WORKDIR /app

COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 開放端口
EXPOSE 8000

# 啟動應用程序
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

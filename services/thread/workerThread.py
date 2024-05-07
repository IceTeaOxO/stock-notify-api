import threading
import time


class WorkerThread(threading.Thread):
    def __init__(self, thread_name, work_function, *args, **kwargs):
        super().__init__()
        self.name = thread_name
        self.work_function = work_function
        self.args = args
        self.kwargs = kwargs
        self.running = True
        self.previous_quotes = {}  # 用於存儲策略的狀態，如果有需要
        try:
            self.webhook_time = float(kwargs.get("webhook_time", 300))
        except ValueError:
            self.webhook_time = 300

    def run(self):
        print(f"Thread {self.name} starting with data: {self.kwargs}")

        while self.running:
            if self.work_function.__name__ == "momentum_strategy":
                self.kwargs["previous_quotes"] = self.previous_quotes
                # 更新 previous_quotes
                self.previous_quotes = self.work_function(**self.kwargs)
                # 將 previous_quotes 傳遞給策略函數

            else:
                print("Function not found")

            time.sleep(self.webhook_time)
        print(f"Thread {self.name} stopped")

    def stop(self):
        self.running = False

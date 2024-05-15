from services.thread.workerThread import WorkerThread
from services.strategy.momentum_strategy import momentum_strategy


class ThreadManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ThreadManager, cls).__new__(cls)
            # 在這裡初始化 ThreadManager 的屬性
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'threads'):
            self.threads = {}

    def add_thread(self, thread_name, thread):
        """添加線程到管理器"""
        self.threads[thread_name] = thread

    def remove_thread(self, thread_name):
        """從管理器移除線程"""
        if thread_name in self.threads:
            del self.threads[thread_name]

    def start_thread(self, file_data):

        # 之後應該是輸入檔案名稱，透過讀檔案的方式取得資料
        """根據傳入的file data開啟對應的線程"""
        thread_name = file_data.get('file_name')
        strategy = file_data.get('strategy')
        work_function_name = strategy.get('strategy_name')
        parameters = strategy.get('parameters', {})
        data = file_data.get('data', [])
        webhook_url = file_data.get('webhook_url')
        webhook_time = file_data.get('webhook_time')

        # print(f"Starting thread for {thread_name}")
        # print(f"Strategy: {strategy}")
        print(f"Work function name: {work_function_name}")
        # print(f"Parameters: {parameters}")
        # print(f"Data: {data}")
        # print(f"Webhook URL: {webhook_url}")
        # print(f"Webhook Time: {webhook_time}")

        # 使用反射機制獲取函數對象
        # 取得全域變數中的函數對象
        work_function = globals().get(work_function_name)
        if work_function is None:
            print(f"Function {work_function_name} not found.")
            return

        # 將參數打包成args並傳遞給WorkerThread
        args = tuple(parameters.values())
        # 將所有參數包裝成kwargs並傳遞給WorkerThread
        kwargs = {
            **parameters,
            'data': data,
            'webhook_url': webhook_url,
            'webhook_time': webhook_time
            }

        # 這邊直接傳入對應的函式，而非函式名稱
        thread = WorkerThread(thread_name, work_function, *args, **kwargs)
        self.add_thread(thread_name, thread)
        thread.start()

    def stop_thread_by_name(self, name):
        """根據名稱優雅地中斷線程"""
        thread = self.threads.get(name)
        if thread:
            thread.stop()
            self.remove_thread(name)
            print(f"Thread for {name} has been requested to stop.")
        else:
            print(f"No thread found with name {name}")

    def get_thread_names(self):
        """獲取當前存在的線程名稱列表"""
        thread_names = list(self.threads.keys())
        print(self.threads.keys())
        return thread_names

    def stop_all_threads(self):
        """停止所有線程"""
        for thread_name, thread in self.threads.items():
            thread.stop()
            self.remove_thread(thread_name)
            print(f"Thread for {thread_name} has been requested to stop.")
        print("All threads have been requested to stop.")

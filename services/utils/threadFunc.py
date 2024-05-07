import threading
import time

class ThreadWithStopFlag(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(ThreadWithStopFlag, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        while not self.stopped():
            # 你的线程执行代码
            print("Thread is running...")
            time.sleep(1)  # 模拟工作

            
            # 检查停止标志
            if self.stopped():
                break
        print("Thread is gracefully stopping")

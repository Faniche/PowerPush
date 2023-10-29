import platform
import threading
import time
from queue import Queue

from src.common.Constant import ModuleName
from src.common.Message import Message


class Module(threading.Thread):
    def __init__(self, name: ModuleName):
        super().__init__(name=name)
        self.os_type = platform.system()
        self.rcv_queue = Queue()
        self.snd_queue = Queue()
        self.rcv_queue_lock = threading.Lock()
        self.snd_queue_lock = threading.Lock()

    def run(self):
        heartbeat_thread = threading.Thread(target=self.thrd_func_heart_attack)
        heartbeat_thread.start()

    def thrd_func_heart_attack(self):
        while True:
            self.snd_queue_lock.acquire()
            self.snd_queue.put(Message(self.name))
            self.snd_queue_lock.release()
            time.sleep(10)
    #
    # def stop(self):
    #     raise Exception("method pure virtual")
    #
    # def clear(self):
    #     raise Exception("method pure virtual")

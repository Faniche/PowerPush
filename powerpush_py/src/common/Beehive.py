import platform
import threading
import time
from queue import Queue


class Beehive:
    def __init__(self):
        self.modules = dict()
        self.message_quque = Queue()


    def run(self):
        for module in self.modules:
            module.start()

    def dispatch_message(self):
        rcv_thrd = threading.Thread(target=self.thrd_func_rcv_msg_from_modules)
        rcv_thrd.start()

        dispatcher_thrd = threading.Thread(target=self.thrd_func_rcv_msg_from_modules)
        dispatcher_thrd.start()

    def thrd_func_rcv_msg_from_modules(self):
        while True:
            for _, module in self.modules:
                module.snd_queue_lock.acquire()
                while not module.snd_queue.empty():
                    self.message_quque.put(module.snd_queue.get())
                module.snd_queue_lock.release()
            time.sleep(1)

    def thrd_func_dispatch_msg_to_modules(self):
        while True:
            while not self.message_quque.empty():
                msg = self.message_quque.get()
                self.modules[msg.dst_module_name].rcv_queue_lock.acquire()
                self.modules[msg.dst_module_name].rcv_queue.put(msg)
                self.modules[msg.dst_module_name].rcv_queue_lock.release()
            time.sleep(1)
import threading
import sys
import time

def thread(fun):
    def decorator(*args, **kwargs):
        try:
            thread = threading.Thread(target=fun, args=(*args, ))
            thread.daemon = True
            thread.start()
            controller.append_thread(str(fun).split()[1])

        except Exception as error:
            print(error, file=sys.stderr), sys.exit()
    return decorator

def thread_v(fun):
    def decorator(*args, **kwargs):

        from multiprocessing.pool import ThreadPool
        pool = ThreadPool(processes=10)

        return pool.apply_async(fun, *args).get()
    return decorator

def return_threads_name():
    return controller.threads_name

def return_threads():
    return len(controller.threads_name) 

class thread_controller:

    def __init__(self):
        self.threads = 0
        self.threads_name = []

    def append_thread(self, func_name):
        self.threads_name.append(func_name)


controller = thread_controller()

    
#!/usr/bin/env python3

import threading
import time

class Mythread(threading.Thread):
    def __init__(self, myId, count, mutex):
        self.myId = myId
        self.count = count
        self.mutex = mutex
        super().__init__()

    def run(self):
        for i in range(self.count):
            with self.mutex:
                print('[%s] => %s' % (self.myId, i))

stdoutmutex = threading.Lock()
threads = []

for i in range(10):
    thread = Mythread(i, 100, stdoutmutex) # создать/запустить 10 потоков
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
print('Main thread exiting.')

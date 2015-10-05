#!/usr/bin/env python3

import threading
import time

count = 0
def adder(addlock):
    global count
    with addlock:
        count = count + 1 # изменяет глобальную переменную
    time.sleep(0.05)
    with addlock:
        count = count + 1 # глобальные объекты и переменные

addlock = threading.Lock()
threads = []
for i in range(10**5):
    thread = threading.Thread(target=adder, args=(addlock,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
print(count)

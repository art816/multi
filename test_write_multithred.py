#!/usr/bin/env python3

from threading import Thread
import time

start = time.time()
def writer(filename, n):
    with open(filename, 'w') as fout:
        for i in range(n):
            fout.write('1\n')

t1 = Thread(target=writer, args=('test2.txt', 500000,))
t2 = Thread(target=writer, args=('test3.txt', 500000,))

t1.start()
t2.start()
t1.join()
t2.join()
print('time == ', time.time() - start)


#!/usr/bin/env python3

import _thread
import time


mutex = _thread.allocate_lock()

def counter(my_id, count):
    for i in range(count):
        time.sleep(1)
        mutex.acquire()
        print("child ", my_id, i)
        mutex.release()

def parent():
    for i in range(5):
        _thread.start_new_thread(counter, (i, 5))


if __name__ == "__main__":
    parent()
    time.sleep(6)
    print("Main thread ex")

#!/usr/bin/env python3

import threading

def writer(tr_id, event_for_wait, event_for_set):
    x = 0
    for i in range(10):
        event_for_wait.wait() # wait for event
        event_for_wait.clear() # clean event for future
        print(x, tr_id)
        x += 1
        event_for_set.set() # set event for neighbor thread

if __name__ == '__main__':
# init events
    e1 = threading.Event()
    e2 = threading.Event()
    e3 = threading.Event()

# init threads
    t1 = threading.Thread(target=writer, args=(0, e1, e2))
    t2 = threading.Thread(target=writer, args=(1, e2, e3))
    t3 = threading.Thread(target=writer, args=(2, e3, e1))

# start threads
    t1.start()
    t2.start()
    t3.start()

    e1.set() # initiate the first event

# join threads to the main thread
    t1.join()
    t2.join()
    t3.join()

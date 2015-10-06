#!/usr/bin/env python3

numconsumers = 2
numproducers = 4
nummessages = 4
# количество потоков-потребителей
# количество потоков-производителей
# количество сообщений, помещаемых производителем

import threading, queue, time

def producer(idnum, dataqueue):
    for msgnum in range(nummessages):
        time.sleep(idnum)
        dataqueue.put('[producer id=%d, count=%d]' % (idnum, msgnum))

def consumer(idnum, dataqueue, safeprint):
    while True:
        time.sleep(0.1)
        with safeprint:
            queue_len = dataqueue.qsize()
            if queue_len > 0:
                data = dataqueue.get(block=False)
                print('queue_len', queue_len, 'consumer', idnum, 'got =>', data)

if __name__ == '__main__':
    safeprint = threading.Lock() # в противном случае вывод может
# перемешиваться
    dataqueue = queue.Queue()
    thread_list = []
# общая очередь неограниченного размера
    for i in range(numconsumers):
        thread = threading.Thread(target=consumer, args=(i, dataqueue, safeprint))
        thread.daemon = True
        thread.start()
    for i in range(numproducers):
        thread = threading.Thread(target=producer, args=(i, dataqueue))
        thread_list.append(thread)
        thread.start()
    for thread in thread_list:
        thread.join()
        print(thread.name)
    print('Main thread exit.')

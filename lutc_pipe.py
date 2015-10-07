__author__ = 'art'

import os
import time
import _thread


def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz) # заставить родителя подождать
        msg = ('Spam %03d\n' % zzz).encode() # каналы – двоичные файлы
        os.write(pipeout, msg) # отправить данные родителю
        zzz = (zzz+1) % 5 # переход к 0 после 4

def parent():
    pipein, pipeout = os.pipe() # создать канал с 2 концами
    print(type(pipein), type(pipeout), pipein, pipeout)
    # threading.Thread(target=child, args=(pipeout,)).start()
    _thread.start_new_thread(child, (pipeout,))
    # if os.fork() == 0: # создать копию процесса
    #     child(pipeout) # в копии вызвать child
    # else: # в родителе слушать канал
    # pipein = os.fdopen(pipein)
    while True:
        line = os.read(pipein, 4) # остановиться до получения данных
        # line = pipein.readline()[:-1]
        print('Parent %d got [%s] at %s' % (os.getpid(), line,
                                            time.time()))

parent()
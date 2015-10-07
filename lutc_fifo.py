"""
именованные каналы; функция os.mkfifo недоступна в Windows (без Cygwin);
здесь нет необходимости использовать прием ветвления процессов, потому что
файлы каналов fifo являются внешними по отношению к процессам -- совместное
использование дескрипторов файлов в родителе/потомке здесь неактуально;
"""
import os, time, sys
fifoname = '/tmp/pipefifo'
# имена должны быть одинаковыми

def child():
    pipeout = os.open(fifoname, os.O_WRONLY) # открыть fifo как дескриптор
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('N=%s Spam %03d\n' % (sys.argv[1], zzz)).encode() # был открыт в двоичном режиме
        os.write(pipeout, msg)
        zzz = (zzz+1) % 5

def parent():
    pipein = open(fifoname, 'r')
# открыть fifo как текстовый файл
    while True:
        print(pipein.errors)
        line = pipein.readline()[:-1]
        # блокируется до отправки данных
        print('Parent %d got "%s" at %s' % (os.getpid(), line, time.time()))

if __name__ == '__main__':
    if not os.path.exists(fifoname):
        os.mkfifo(fifoname)
    if len(sys.argv) == 1:
        parent()
    # если нет аргументов - запустить как родительский процесс
    else:
    # иначе - как дочерний процесс
        child()

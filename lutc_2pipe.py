"""
запускает дочерний процесс/программу, соединяет свои потоки stdin/stdout
с потоками stdout/stdin дочернего процесса -- операции чтения и записи на
стороне родительского процесса отображаются на стандартные потоки ввода-вывода
дочерней программы; напоминает соединение потоков с помощью модуля subprocess;
"""

import os, sys

def spawn(prog, *args):
# имя программы, аргументы командной строки
    stdinFd = sys.stdin.fileno()
# получить дескрипторы потоков
    stdoutFd = sys.stdout.fileno()
# обычно stdin=0, stdout=1
    parentStdin, childStdout = os.pipe()
    childStdin, parentStdout = os.pipe()
    pid = os.fork()
    if pid:
        os.close(childStdout)
        os.close(childStdin)
        os.dup2(parentStdin, stdinFd)
        os.dup2(parentStdout, stdoutFd)
    else:
        os.close(parentStdin)
        os.close(parentStdout)
        os.dup2(childStdin, stdinFd)
        os.dup2(childStdout, stdoutFd)
        args = (prog,) + args
        os.execvp(prog, args)
        assert False, "execvp failed!"

if __name__ == '__main__':
    mypid = os.getpid()
    spawn('python', 'pipes_testchild.py', 'spam')

    print('Hello_1_from_parent', mypid)
    sys.stdout.flush()

    #reply = sys.stdin.readline()
    reply = input()
    sys.stderr.write('1 Parent got: "{}"\n'.format(reply))

    print('Hello_2_from_parent', mypid)
    sys.stdout.flush()

    reply = input()
    sys.stderr.write('3 Parent got: "%s"\n' % reply)

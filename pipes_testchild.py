import os, time, sys

mypid = os.getpid()
parentpid = os.getppid()
sys.stderr.write('Child %d of %d got arg: "%s"\n' %
(mypid, parentpid, sys.argv[1]))

for i in range(2):
    time.sleep(1)
    recv = sys.stdin.readline()
    time.sleep(1)
    send = 'Child %d got: [%s]' % (mypid, recv[:-1])
    print(send)
    sys.stdout.flush()

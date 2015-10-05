#!/usr/bin/env python3

import time

start = time.time()
with open('test1.txt', 'w') as fout:
    for i in range(1000000):
        fout.write('1\n')
print('time == ', time.time() - start)

#!/usr/bin/env python3

import os
import time

def child_counter(count):
    os.execlp('python3', 'python3', 'child_program.py', str(count))
    assert(False, "Can not start program")

def parent():
    for i in range(16):
        newpid = os.fork()
        if newpid == 0:
            child_counter(i)
            os._exit(0)
        else:
            print("Parent ", os.getpid(), newpid)

if __name__ == "__main__":
    parent()

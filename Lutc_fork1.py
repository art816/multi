#!/usr/bin/env python3

import os
import time

def child_counter(count):
    for i in range(count):
        n = 2
        for j in range(10**6):
           n = (n**2) % 10**20
        print("Child id={} i={} n={}".format(os.getpid(), i, n))

def parent():
    for i in range(16):
        newpid = os.fork()
        if newpid == 0:
            child_counter(5)
            os._exit(0)
        else:
            print("Parent ", os.getpid(), newpid)

if __name__ == "__main__":
    parent()

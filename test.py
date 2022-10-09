# Warning This file is for testing the data structures 

import DSPro.List.CList as CList
import threading as th
import multiprocessing as ps
import time
import os
def append(g : CList, value : list):
    for j in value:
        print(th.current_thread().name)
        g.append(j)

def sort(g: CList):
    print(th.current_thread().name)
    g.sort(key = lambda x: -x)

a = CList()

thread1 = th.Thread(target=append, args=(a, list(range(0,10)),))
thread2 = th.Thread(target=append, args=(a, list(range(10,20)),))
thread3 = th.Thread(target=sort, args=(a,))
thread1.start()
thread2.start()
thread3.start()

time.sleep(5)
print(a)


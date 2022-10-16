import threading as th

class CDNode:
    def __init__(self, value : any, prev : 'CDNode' = None, next : 'CDNode' = None):
        self.value = value
        self.prev = prev
        self.next = next
        self.__lock = th.RLock()

    def acquire(self):
        self.__lock.acquire()

    def release(self):
        self.__lock.release()

     


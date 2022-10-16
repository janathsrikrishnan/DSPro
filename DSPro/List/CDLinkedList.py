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


class CDLinkedList:
    
    def __init__(self, root : CDNode = None):
        self.__root = None
        start = CDNode("#Start#")
        end = CDNode("#End#")    
        if root:
            self.__root = root
            self.__root.prev = start
            self.__root = self.__root.prev
            head = self.__root
            while head.next:
                head = head.next
            head.next = end
        else:
            self.__root = start
            self.__root.next = end

        
    def __getitem__(self, index) -> int:
        pass

    def __len__(self) -> int:
        pass

    def addAt(self, item : 'any', index : int) -> bool:
        pass

    def addFront(self, item : 'any') -> bool:
        pass

    def addEnd(self, item : 'any') -> bool:
        pass
        
    def contains(self) -> bool:
        pass
    
    def pop(self, index : int = -1) -> 'any':
        pass

    def remove(self, item : 'any') -> bool:
        pass
    
    def root(self) -> CDNode:
        """ return the root of the list"""
        return self.__root


    def tolist(self) -> list:
        pass



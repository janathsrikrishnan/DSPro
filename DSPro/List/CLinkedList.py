import threading as th

class CNode:
    def __init__(self, value=None, next=None):
        self.__value = value
        self.next = next

    def next(self):
        return self.next

    def value(self):
        return self.__value
    

class CLinkedList:
    """ Singly Linked List with concurrent support """
    def __init__(self, root : CNode = None):
        if not root:
            self.__root = CNode(-float('inf'))
            self.__root.next = CNode(float('inf'))
            
        else:
            self.__root = root
        self.__length = 0       
        self.Update = True  # if the list is updated it is marked to update the lenght in another thread
        self.__lock =  th.RLock()

    def addFront(self, item : 'any') -> bool:
        """ add the new element to the front in the in the linked list """
        self.__lock.acquire()
        try:
            aux = CNode(item)
            aux.next = self.__root.next()
            self.__root.next = aux
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.__lock.release()

    def addEnd(self, item : 'any') -> bool:
        """ add the element end to linked list """
        pass
    
    def addAt(self, index : int, item : 'any') -> bool:
        """ add the element at specified position if it is between the length of the list otherwise add to end """
        pass
    
    def contains(self, item : 'any') -> int:
        """ check whether the element is present in the linked list """
        pass

    def pop(self, index : int = -1) -> CNode:
        """ remove and return the node at given position default last"""
        pass

    def remove(self, item : 'any') -> bool:
        """ remove the element """
        pass
    
    def root(self):
        """ return the root of the list"""
        return self.__root

    
    
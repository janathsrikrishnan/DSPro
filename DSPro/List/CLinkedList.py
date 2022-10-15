import threading as th

class CNode:
    def __init__(self, value=None, next=None):
        self.__value = value
        self.next = next
        self.__lock = th.RLock()

    def next(self):
        return self.next

    def acquire(self):
        self.__lock.acquire()

    def release(self):
        self.__lock.release()

    def value(self):
        return self.__value
    

class CLinkedList:
    """ Singly Linked List with concurrent support """
    def __init__(self, root : CNode = None):
        if not root:
            self.__root = CNode("#Start#")
            self.__root.next = CNode("#End#")
            
        else:
            self.__root = root

        # for future ideas
        # self.__length = 0       
        # self.Update = True  # if the list is updated it is marked to update the lenght in another thread
        

    def addFront(self, item : 'any') -> bool:
        """ add the new element to the front in the in the linked list """
        self.__root.acquire()
        try:
            aux = CNode(item)
            aux.next = self.__root.next()
            self.__root.next = aux
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.__root.release()

    def addEnd(self, item : 'any') -> bool:
        """ add the element end to linked list """
        prev = self.__root
        prev.acquire()
        try:
            while (str(prev.next().value()) != "#End#"):
                prev.release()
                prev = prev.next()
                prev.acquire()
            aux = CNode(item)
            aux.next = prev.next()
            prev.next = aux.next()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            prev.release()

    def addAt(self, index : int, item : 'any') -> bool:
        """ add the element at specified position if it is between the length of the list otherwise add to end """
        prev = self.__root
        prev.acquire()
        try:
            while (index and str(prev.next().value()) != "#End#"):
                prev.release()
                index -= 1
                prev = prev.next()
                prev.acquire()
            aux = CNode(item)
            aux.next = prev.next()
            prev.next = aux.next()
        except Exception as e:
            print(e)
            return False
        finally:
            prev.release()
    
    def contains(self, item : 'any') -> int:
        """ check whether the element is present in the linked list """
        

    def pop(self, index : int = -1) -> CNode:
        """ remove and return the node at given position default last"""
        pass

    def remove(self, item : 'any') -> bool:
        """ remove the element """
        pred = self.__root
        pred.acquire()
        
        try:
            curr = pred.next
            curr.acquire()
            found = False
            while (str(curr.value()) != "#End#"):
                if str(curr.value()) == str(item): 
                    found = True
                    break
                pred.release()
                pred = curr
                curr = curr.next
                curr.release()
            if found:
                pred.next = curr.next
                return True
        except Exception as e:
            return False
        finally:
            curr.release()
            pred.release()
            
    def root(self):
        """ return the root of the list"""
        return self.__root

    
    
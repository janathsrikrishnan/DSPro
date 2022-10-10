import copy
import threading as th

class CList:
    def __init__(self, value : list = []):
        # list variable
        self.__list = value
        
        #reentrant lock
        self.__lock = th.RLock()        

    def __str__(self) -> str:
        self.__lock.acquire()
        try:
            return " ".join([str(i) for i in self.__list])
        except Exception as e:
            print(e)
            return ""
        finally:
            self.__lock.release()

    def __getitem__(self, index) -> 'any':
        self.__lock.acquire()
        try:
            return self.__list[index]
        except Exception as e:
            print(e)
            return -1
        finally:
            self.__lock.release()

    def __len__(self) -> int:
        self.__lock.acquire()
        try:
            return len(self.__list)
        except Exception:
            return -1
        finally:
            self.__lock.release()

    def __delitem__(self, index : int) -> bool:
        self.__lock.acquire()
        try:
            del self.__list[index]
            return True
        except Exception as e:
            return False
        finally:
            self.__lock.release()

    def append(self, value : "any") -> bool:
        # acquire the lock
        self.__lock.acquire()
        # append the value
        try:
            self .__list.append(value)
            return True
        except Exception as e:
            print(e)
        finally:
        # release the lock
            self.__lock.release()

    
    def index(self, value : 'any') -> int:
        """ Return the index of the element if present in the array.
             if present in the list. Otherwise return -1"""
        self.__lock.acquire()
        try:
            return self.__list.index(value)
        except Exception as e:
            return -1
        finally:
            self.__lock.release()
    
    def insert(self, index : int, value : "any") -> bool:
        self.__lock.acquire()
        try:
            self.__list.insert(index, value)
            return True
        except Exception:
            return False
        finally:
            self.__lock.release()

    def clear(self) -> bool:
        """ Clear the clist """
        self.__lock.acquire()
        try:
            self.__list.clear()
            return True
        except Exception:
            return False
        finally:
            self.__lock.release()

    def copy(self) -> 'any':
        """ create a copy of the clist and return the clist. otherwise return None """
        self.__lock.acquire()
        try:
            aux = copy.deepcopy(self.__list)
            auxClist = CList(aux)
            return auxClist
        except Exception as e:
            return None
        finally:
            self.__lock.release()

    def count(self, value : 'any') -> int:
        """ return the count of the element present in the clist """
        self.__lock.acquire()
        try:
            return self.__list.count(value)
        except Exception as e:
            return -1
        finally:
            self.__lock.release()

    def pop(self, index=-1) -> int | None:
        """ pop and return the item from the list if list is not empty.
             Otherwise return None"""
        self.__lock.acquire()
        try:
            return self.__list.pop(index)
        except Exception as e:
            return None
        finally:
            self.__lock.release()

    def remove(self, value : 'any') -> bool:
        """ Remove the element if present and return True. otherwise it return False"""
        self.__lock.acquire()
        try:
            self.__list.remove(value)
            return True
        except Exception as e:
            return False
        finally:
            self.__lock.release()

    def sort(self, key = None, reverse = False) -> None:
        """ sort the element present in the clist inplace """
        self.__lock.acquire()
        try:
            if (key and reverse):
                self.__list.sort(key = key, reverse = True)
            elif reverse:
                self.__list.sort(reverse = True)
            elif key:
                self.__list.sort(key = key)
            else:
                self.__list.sort()
        except Exception as e:
            pass
        finally:
            self.__lock.release()

    def tolist(self) -> list:
        """ return the list """
        return self.__list
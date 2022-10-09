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


    def insert(self, index : int, value : "any") -> bool:
        self.__lock.acquire()
        try:
            self.__list.insert(index, value)
            return True
        except Exception:
            return False
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
            # print("")  

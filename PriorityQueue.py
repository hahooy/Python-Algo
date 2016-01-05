'''
Created on Dec 22, 2015

@author: hahooy1
>>> import PriorityQueue
>>> q = PriorityQueue.PriorityQueue()
>>> for i in range(10):
...     q.insert(i)
... 
>>> assert q.maximum() == 9, 'maximum value in the queue should be 9'
'''

class PriorityQueue(object):
    '''
    a maximum first priority queue ADT implemented using a heap
    '''    

    def __init__(self, size = 10):
        '''
        Constructor
        '''
        self.A = [None] * size
        self.size = 0
       
    def  maximum(self):
        return self.A[1]
    
    def extractMax(self):
        if self.size < 1:
            print("the queue is empty")
            quit()
            
        self.__swap(1, self.size)
        maxElement = self.A[self.size]
        self.A[self.size] = None
        self.size -= 1
        self.__sink(1)
        return maxElement
    
    def insert(self, key):
        if self.size == len(self.A) - 1:
            temp = self.A[:]
            self.A = [None] * (2 * len(temp))
            self.A[:self.size + 1] = temp[:]
        self.size += 1
        self.A[self.size] = key
        self.__swim(self.size)
        
    def __sink(self, i):
        while i <= self.size // 2:
            j = 2 * i
            if j < self.size and self.A[j] < self.A[j + 1]: # choose the larger child
                j += 1
            if self.A[i] >= self.A[j]:
                break
            self.__swap(i, j)
            i = j
            
    def __swim(self, i):
        while i > 1:
            parent = i // 2
            if self.A[i] <= self.A[parent]:
                break
            self.__swap(i, parent)
            i = parent
            
    def __swap(self, i, j):
        self.A[i], self.A[j] = self.A[j], self.A[i]
            
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    """q = PriorityQueue()
    for i in range(10):
        q.insert(i)
    print(q.A)
    for _ in range(10):
        print(q.extractMax())"""
            
            
            
                
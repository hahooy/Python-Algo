'''
Created on Dec 30, 2015

@author: hahooy1
'''

class MinQueue(object):
    '''
    classdocs
    '''


    def __init__(self, N = 10):
        '''
        Constructor
        '''
        self.capacity = N + 1
        self.A = [None] * self.capacity
        self.size = 0
        
    def insert(self, x):
        self.size += 1
        if self.size + 1 >= self.capacity:
            self.__expand()        
        self.A[self.size] = x        
        
    def __swim(self, i):
        while i > 1:
            j = i // 2
            if self.A[i] < self.A[j]:
                self.__swap(i, j)
                
    def __swap(self, i, j):
        self.A[i], self.A[j] = self.A[j], self.A[i]
        
    def __expand(self):
        """ double the size of the queue """
        self.capacity *= 2
        temp = [None] * self.capacity
        temp[:len(self.A)] = self.A[:]
        self.A = temp
        
    def __str__(self, *args, **kwargs):
        return str(self.A)
    
if __name__ == "__main__":
    q = MinQueue()
    q.insert(1)
    q.insert(2)
    print(q)
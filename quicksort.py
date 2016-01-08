"""
>>> import quicksort
>>> a = [5,4,3,2,1,5,9,2,1,3]
>>> q = quicksort.QuickSort()
>>> q.sort(a)
>>> q.isSorted(a)
True
"""
from random import random

class QuickSort:
    def __init__(self):
        pass

    def sort(self, a):
        """ quick sort """
        self.sorthelper(a, 0, len(a) - 1)
        
    def sorthelper(self, a, lo, hi):
        if lo >= hi:
            return
        pivot_index = lo + int(random() * (hi - lo + 1))
        self.swap(a, lo, pivot_index)
        j = self.partition(a, lo, hi)
        self.sorthelper(a, lo, j - 1)
        self.sorthelper(a, j + 1, hi)

    def partition(self, a, lo, hi):
        pivot = a[lo]
        i, j = lo + 1, hi
        while True:
            while i < hi and a[i] < pivot:
                i += 1
            while j > lo and a[j] > pivot:
                j -= 1
            if i >= j:
                break  
            self.swap(a, i, j)
            i, j = i + 1, j - 1
        self.swap(a, lo, j)
        return j
    
    def swap(self, a, i, j):
        a[i], a[j] = a[j], a[i]

    def isSorted(self, a):
        """ test if input array a is sorted """
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                return False
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    a = [0] * 1000
    s = QuickSort()
    for i in range(0, len(a)):
        a[i] = int(random() * 100)
    s.sort(a)
    print(a)

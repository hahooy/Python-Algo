"""
>>> import quicksort
>>> a = [5,4,3,2,1]
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
        if lo >= hi: ### no need to sort an array with less than one element
            return
        pivot_index = lo + int(random() * (hi + 1 - lo))
        self.swap(a, lo, pivot_index)
        j = self.partition(a, lo, hi)
        self.sorthelper(a, lo, j - 1)
        self.sorthelper(a, j + 1, hi)

    def partition(self, a, lo, hi):
        """ partition function, return the index of partition element """
        pivot = a[lo] ### pick the first element as the pivot
        i, j = lo, hi + 1

        while True:
            while i < hi:
                i += 1
                if a[i] >= pivot:
                    break
            while j > lo:
                j -= 1
                if a[j] <= pivot:
                    break
            if i >= j:
                break
            self.swap(a, i, j)

        self.swap(a, lo, j)
        return j

    def swap(self, a, i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    def isSorted(self, a):
        """ test if input array a is sorted """
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                return False
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()

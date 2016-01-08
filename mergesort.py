""" sorting algorithm using merge sort
>>> from mergesort import MergeSort
>>> s = MergeSort()
>>> a = [5,4,3,2,1]
>>> s.sort(a)
>>> a
[1, 2, 3, 4, 5]
"""

from random import random

class MergeSort:
    def __init__(self):
        pass

    def sort(self, a):
        aux = a[:]
        self.sortHelper(a, aux, 0, len(a) - 1)

    def sortHelper(self, a, aux, lo, hi):
        if lo >= hi:
            return
        mid = lo + (hi - lo) // 2
        self.sortHelper(a, aux, lo, mid)
        self.sortHelper(a, aux, mid + 1, hi)
        self.merge(a, aux, lo, mid, hi)
        
    def merge(self, a, aux, lo, mid, hi):
        aux[lo:hi + 1] = a[lo:hi + 1]
        i, j = lo, mid + 1
        for k in range(lo, hi + 1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif aux[i] < aux[j]:
                a[k] = aux[i]
                i += 1
            else:
                a[k] = aux[j]
                j += 1
        
    def __isSorted__(self, a, lo, hi):
        for i in range(lo + 1, hi + 1):
            if a[i] < a[i-1]:
                return False
        return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    a = []
    s = MergeSort()
    for i in range(100):
        a.append(int(random() * 100))
    s.sort(a)
    print(a)

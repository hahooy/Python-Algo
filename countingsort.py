#!/usr/bin/env python3
""" index counting sort algorithm """
import random

class countingSort(object):
    """ counting sort object """
    def __init__(self, k):
        """ assumes that each of the n input elements is an integer in the range 0 to k - 1 """
        self.k = k

    def sort(self, a):
        b, counters = [0] * len(a), [0] * self.k
        for i in a:
            if type(i) is str:
                i = ord(i) # account for charaters
            counters[i] += 1
        for i in range(1, len(counters)):
            counters[i] += counters[i - 1]
        for i in range(0, len(a)):
            k = a[i]
            if type(k) is str:
                k = ord(k)
            b[counters[k] - 1] = a[i]
            counters[k] -= 1
        for i in range(0, len(a)):
            a[i] = b[i]
                     
def test():
    n, k = 100, 10
    a = [0] * n
    sorting = countingSort(k)

    for i in range(0, n):
        a[i] = int(random.random() * k)

    sorting.sort(a)
    assert(isSorted(a))
    print(a)

def test2():
    n, k = 100, 256
    a = [0] * n
    sorting = countingSort(k)

    for i in range(0, n):
        a[i] = chr(int(random.random() * 26) + ord('A'))

    sorting.sort(a)
    assert(isSorted(a))
    print(a)

def isSorted(a):
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            return False
    return True    
    
if __name__ == "__main__":
    test()
    test2()

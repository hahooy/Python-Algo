#!/usr/bin/env python3
""" index counting sort algorithm """
from random import random

class CountingSort:
    def __init__(self, k):
        self.k = k

    def sort(self, a):
        count = [0] * self.k # an auxilary array for the counters
        for i in a:
            count[i] += 1
        m = 0
        for i in range(0, self.k):
            for j in range(0, count[i]):
                a[m] = i
                m += 1

def test():
    a = [0] * 10
    for i in range(0, len(a)):
        a[i] = int(random() * 10)
    s = CountingSort(10)
    s.sort(a)
    print(a)

if __name__ == "__main__":
    test()

""" sorting algorithm using merge sort """

import random

class MergeSort:
    def __init__(self):
        pass

    def sort(self, a):
        aux = []
        for i in a:
            aux.append(i)
        self.sortHelper(a, aux, 0, len(a) - 1)

    def sortHelper(self, a, aux, lo, hi):
        if lo >= hi:
            return

        mid = lo + (hi - lo) // 2
        self.sortHelper(a, aux, lo, mid)
        self.sortHelper(a, aux, mid + 1, hi)
        self.merge(a, aux, lo, mid, hi)

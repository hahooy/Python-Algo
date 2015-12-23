""" insertion sort algorithm """

from random import random

class InsertionSort:
    def sort(self, a):
        for i in range(1, len(a)):
            j = i
            while j > 0 and a[j] < a[j-1]:
                self.swap(a, j, j-1)
                j -= 1
        assert(self.__isSorted__(a))
                
    def swap(self, a, i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    def __isSorted__(self, a):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                return False
        return True

if __name__ == "__main__":
    a = []
    s = InsertionSort()
    for i in range(100):
        a.append(int(random() * 100))

    s.sort(a)
    print(a)

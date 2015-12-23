""" sorting an array using heap property """
from random import random


def sort(a):
    N = len(a)
    heapify(a)
    # sort down
    while N > 1:
        exch(a, 1, N)
        N -= 1
        sink(a, 1, N)

def heapify(a):        
    N = len(a)
    k = N // 2
    while k > 0:
        sink(a, k, N)
        k -= 1

def sink(a, k, N):
    while k <= N // 2:
        j = 2 * k
        if j < N and less(a,j,j+1):
            j = j+1
        if not less(a, k, j):
            break
        exch(a, j, k)
        k = j

def exch(a, i, j):
    temp = a[i-1]
    a[i-1] = a[j-1]
    a[j-1] = temp
    print(a)

def less(a, i, j):
    return a[i-1] < a[j-1]

def isSorted(a):
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            return False
    return True

def test():
    a = [6,1,10,2,8,0]
    sort(a)

if __name__ == "__main__":
    test()            

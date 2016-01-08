#! /usr/bin/env python3

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def fibTR(n):
    return __fibTR_helper(n, 0, 1)

def __fibTR_helper(n, a, b):
    if n == 0:
        return a
    return __fibTR_helper(n - 1, b, a + b)
    
def fibDP(n):
    i, j = 0, 1
    while n > 0:
        i, j = j, i + j
        n -= 1
    return i

if __name__ == "__main__":
    print(fibDP(10))
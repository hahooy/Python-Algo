#! /usr/bin/env python3

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibTR(n):
    return __fibTR_helper(n, 0, 1)

def __fibTR_helper(n, a, b):
    if n == 0:
        return a
    else:
        return __fibTR_helper(n - 1, b, a + b)

def fibDP(n):
    a, b = 0, 1

    while n != 0:
        a, b = b, a + b
        n -= 1

    return a
        
    

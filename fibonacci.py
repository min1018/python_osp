#!/usr/bin/python
def fib(n):
        a, b = 0, 1
        for i in range(n):
                a, b = b, a + b
                print(a, end=' ')
        print('\nF%d = %d' %(n, a))

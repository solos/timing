#!/usr/bin/env python
#coding=utf-8

from timing import timing

if __name__ == '__main__':

    @timing(1)
    def fib1(n):
        x, y = 0, 1
        while(n):
            x, y, n = y, x+y, n-1
        return x

    fib2 = lambda n: 1 if n <= 2 else fib2(n-1) + fib2(n-2)
    fib3 = lambda n, x=0, y=1: x if not n else fib3(n-1, y, x+y)

    fib1(30)
    timing(1)(fib2)(30)
    timing(1)(fib3)(30)

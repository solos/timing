#!/usr/bin/env python
#coding=utf-8

from functools import partial
from timeit import Timer

__version__ = '0.01'
__author__ = 'solos'
__doc__ = 'Timing is a decorator for timing function.'


def timing(number=1000000, repeat=0):
    '''timing a function, the two args are running times and repeat times'''
    def _timing(func):
        def _timeit(*args, **kwargs):
            if repeat:
                t = Timer(partial(func, *args, **kwargs))
                print 'hello'
                try:
                    print t.repeat(repeat, number)
                except TypeError, e:
                    print 'timing decorator: %s' % e
            else:
                t = Timer(partial(func, *args, **kwargs))
                try:
                    print t.timeit(number)
                except TypeError, e:
                    print 'timing decorator: %s' % e

        return _timeit
    return _timing

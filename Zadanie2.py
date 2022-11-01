#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit

fact_bez_intr = '''
def factorial(n, acc=1):
    if n == 0:
        return acc
    return factorial(n-1, n*acc)
'''

fib_bez_intr = '''
def fib(i, current = 0, next = 1):
    if i == 0:
        return current
    else:
        return fib(i - 1, next, current + next)
'''

fact_s_intr = '''
class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs
def tail_call_optimized(g):
    def func(*args, **kwargs):
        f = sys._getframe()
        while f and f.f_code.co_filename == f:
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs
    func.__doc__ = g.__doc__
    return func
@tail_call_optimized
def factorial(n, acc=1):
    if n == 0:
        return acc
    return factorial(n-1, n*acc)
'''

fib_s_intr = '''
class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs
def tail_call_optimized(g):
    def func(*args, **kwargs):
        f = sys._getframe()
        while f and f.f_code.co_filename == f:
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs
    func.__doc__ = g.__doc__
    return func
@tail_call_optimized
def fib(i, current = 0, next = 1):
    if i == 0:
        return current
    else:
        return fib(i - 1, next, current + next)
'''

if __name__ == '__main__':
    print('Время вычисления факториала:', timeit.timeit(setup=fact_bez_intr, number=10))
    print('Время вычисления числа Фибоначи:', timeit.timeit(setup=fib_bez_intr, number=10))
    print('Время вычисления факториала с интроспекцией стека:', timeit.timeit(setup=fact_s_intr, number=10))
    print('Время вычисления числа Фибоначи с интроспекцией стека:', timeit.timeit(setup=fib_s_intr, number=10))

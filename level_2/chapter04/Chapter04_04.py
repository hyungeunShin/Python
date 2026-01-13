# 데코레이터

import time

def perf_clock(func):
    def perf_clocked(*args):
        start_time = time.perf_counter()

        result = func(*args)

        end_time = time.perf_counter()

        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)

        print('[%0.5fs] %s(%s) -> %r' % (end_time - start_time, name, arg_str, result)) 

        return result
    
    return perf_clocked

# 데코레이터 미사용
def time_func(seconds):
    time.sleep(seconds)

def sum_func(*numbers):
    return sum(numbers)

ex1 = perf_clock(time_func)
ex2 = perf_clock(sum_func)

ex1(1.5)
ex2(1, 2, 3, 4, 5)

print()

# 데코레이터 사용
@perf_clock
def time_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)

time_func(1.5)
sum_func(1, 2, 3, 4, 5)
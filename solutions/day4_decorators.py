from collections import defaultdict
import functools
import time


# 1. Write a decorator that computes (and displays) execution time for a
# function. Hint: time.time() function returns current time in seconds.
def timeit(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        time_before = time.time()
        return_value = func(*args, **kwargs)
        elapsed_time = time.time() - time_before
        print(f'Execution time for {func.__name__} with args={args} and '
              f'kwargs={kwargs}: {elapsed_time} s.')
        return return_value
    return inner


# 2. Write a decorator function that takes a function as an argument and prints
# the number of times the function has been called.
global_count = 0


def count_exec(func):
    count = 0

    @functools.wraps(func)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        global global_count
        global_count += 1
        print(f'{func.__name__} called {count} times '
              f'(global_count={global_count}).')
        return func(*args, **kwargs)

    return inner


def count_exec_v2(func):
    count = defaultdict(int)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        count[func.__name__] += 1

        print(f'V2. {func.__name__} called {count[func.__name__]} times ')
        return func(*args, **kwargs)

    return inner


@count_exec_v2
@count_exec
@timeit
def long_exec_time(lim1, lim2):
    s = 0
    for i in range(lim1):
        for j in range(lim2):
            s += i * j
    return s


@count_exec_v2
@count_exec
@timeit
def sleepy(s):
    time.sleep(s / 10)


if __name__ == '__main__':
    s1 = long_exec_time(2000, 2000)
    s2 = long_exec_time(5000, 5000)
    print(s1, s2)

    sleepy(3)
    sleepy(4)
    sleepy(1)

# -*- coding: UTF-8 -*-

import sys
import time


def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to


def test(lst=[1, 2, 3]):
    lst.sort()
    return lst


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret_val = func(*args, **kwargs)
        end = time.time() - start
        print("finished {} in {}".format(func.__name__, end))
        return ret_val
    return wrapper


def do_smthg(val):
    void = val ** 27


@timeit
def timing_reversed(L):
    for i in reversed(L):
        do_smthg(i)


@timeit
def timing__slicing(L):
    for i in L[::-1]:
        do_smthg(i)


def main(argv):
    L = list(range(20000))
    timing_reversed(L)
    timing__slicing(L)

if __name__ == '__main__':
    main(sys.argv[1:])

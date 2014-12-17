#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import functools


def myprint(*objects, sep="", end="\n", file=sys.stdout, flush=False):
    file.write(sep.join([str(obj) for obj in objects]) + end)
    if flush:
        file.flush()


def transformateur(func):
    """Transforme une fonction qui ne prend aucun parametre"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        myprint("debut de {}".format(func.__name__))
        res = func(*args, **kwargs)
        myprint("fin de {}".format(func.__name__))
        return res
    return wrapper


@transformateur
def f(arg):
    myprint(5 + arg)


def main(argv):
    f(10)

if __name__ == "__main__":
    main(sys.argv[1:])

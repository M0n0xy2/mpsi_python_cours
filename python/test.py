#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import sys
import functools

def transformateur(func):
    """Transforme une fonction qui ne prend aucun parametre"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("debut de {}".format(func.__name__))
        res = func(*args, **kwargs)
        print("fin de {}".format(func.__name__))
        return res
    return wrapper

@transformateur
def f(arg):
    print(5 + arg)

def main(argv):
    f(10)

if __name__ == "__main__":
    main(sys.argv[1:])

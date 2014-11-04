#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import sys

def syracuse(n):
    if n < 0:
        raise ValueError("n must me positive")

    syrac = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = 3*n + 1
        syrac.append(n)
    return syrac

def main(argv):
    print(syracuse(1))

if __name__ == "__main__":
    main(sys.argv[1:])

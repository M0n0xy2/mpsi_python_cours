#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import random
import math


def random_bilist(size=8, random_fn=random.randint):
    """return a random bidimensional list of size*size int"""
    return [[random_fn(0, size) for _ in range(size)] for _ in range(size)]


def rice_list(size=8, approx_ln=False):
    """return the list of rice number"""
    approx_fn = (lambda x: x) if approx_ln else (lambda x: math.floor(math.log10(x) + 1))
    lines = []
    for y in range(8):
        line = []
        for x in range(8):
                line.append(approx_fn(2**(x + 8*y)))
        lines.append(line)
    return lines


def chessboard(size=8, value=None):
    """just print a nice chessboard of size defaulted to 8 """

    if size < 1:
        raise ValueError("size must be strictly positive")
    if size > 26:
        raise ValueError("size must be lower or equal to 26 "
                         "(we want to print a correct letter)")

    if not value:
        value = [[0]*size]*size

    buffer = "   " + " _____"*size + " \n"
    for y in range(size, 0, -1):
        buffer += "   " + "|     "*size + "|\n"
        buffer += "{:^3}".format(y)
        for x in range(size):
            buffer += "|{:^5}".format(value[y-1][x])
        buffer += "|\n"
        buffer += "   " + "|_____"*size + "|\n"
    buffer += " "*6 + (" "*5).join([chr(c) for c in range(65, 65+size)]) + "\n"
    print(buffer)


def main(argv):
    chessboard(8, rice_list(8, False))


if __name__ == '__main__':
    main(sys.argv[1:])

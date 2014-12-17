#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import sys


def syracuse(n):
    if n < 0:
        raise ValueError("n must me positive")

    syrac = [n]
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        syrac.append(n)
    return syrac


class Node:
    def __init__(self, value):
        self.children = (None, None)
        self.value = value

    def _build(self):
        if self.value != 4 and self.value % 6 == 4:
            self.children = (Node(2 * self.value), Node((self.value - 1) // 3))
        else:
            self.children = (Node(2 * self.value), None)

    def next(self, options, pos):
        self._build()
        pos_to_go = pos
        child_to_go = 0
        if self.children[1]:
            pos_to_go = pos + 1
            if pos >= len(options):
                return [self.value]
            if options[pos] != "0":
                child_to_go = 1
        return [self.value] + self.children[child_to_go].next(options, pos_to_go)


def syracuse_tree(options):
    n = Node(1)
    return n.next(options, 0)


def syracuse_inverse(options, limit=250):
    n = 1
    pos = 0
    syrac = [n]
    while len(syrac) < limit:
        if n != 4 and n % 6 == 4:
            if pos == len(options):
                return syrac
            if options[pos] != "0":
                n = (n-1)//3
            else:
                n = 2*n
            pos += 1
        else:
            n = 2*n
        syrac.append(n)
    return syrac

def syracuse_info(n):
    syra = syracuse(n)
    tdv = len(syra) - 1
    def tdva(syra):
        for pos, item in enumerate(syra[1:]):
            if item <= n:
                return pos
    alt_max = max(syra)
    return dict(temps_de_vol=tdv, temps_de_vol_altitude=tdva(syra), altitude_maximale=alt_max)


def main(argv):
    options = "01"
    # print(syracuse_inverse(options))
    print(syracuse_info(7))

if __name__ == "__main__":
    main(sys.argv[1:])

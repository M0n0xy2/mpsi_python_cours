#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import sys


def eucl(a, b):
    u_p, v_p, u_pp, v_pp = 1, 0, 0, 1
    while b:
        q = a // b
        a, u_p, v_p, b, u_pp, v_pp = b, u_pp, v_pp, a - q * b, u_p - q * u_pp, v_p - q * v_pp
    return a, u_p, v_p


def main(argv):
    p, u, v = eucl(13, 5)
    print((p, u, v))
    print(u * 13 + v * 5)

if __name__ == "__main__":
    main(sys.argv[1:])

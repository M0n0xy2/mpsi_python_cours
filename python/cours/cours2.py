#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""
Juste un module : le module table
"""

import operator


def table(n=7, min=0, max=11):
    """
    écrit quelques tables en Python,
    n peut être entier, zéro, flottant ou complexe
    """
    min, max = sorted([min, max])

    oper = [
        operator.__add__,
        operator.__sub__,
        operator.__mul__,
        operator.__pow__,
        operator.__truediv__,
        operator.__floordiv__,
        operator.__mod__
    ]
    symb = ["+", "-", "*", "**", "/", "//", "%"]
    tble = ""

    for suite in range(2):
        for d in range(min, max+1):
            tble += "\n"
            for i in range(3 * suite, 3 * suite + 3):
                tble += "{:7} {} {:2} = ".format(d, symb[i], n)

                try:
                    res = oper[i](d, n)
                except:
                    res = "erreur"

                if type(res) is float:
                    tble += "{:3.4f}".format(res)
                elif type(res) is int:
                    tble += "{:3}".format(res)
                elif type(res) is complex:
                    tble += "{0.real:3.4f} + {0.imag:3.4f}i".format(res)
                else:
                    tble += "{:10}".format(res)

        tble += "\n"
    print(tble)

if __name__ == '__main__':
    print("table(0)")
    table(0)
    print("table(1+1j)")
    table(1+1j)
    print("table(7, 10, 20)")
    table(7, 10, 20)

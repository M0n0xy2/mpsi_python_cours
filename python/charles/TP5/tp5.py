#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ***************************
# PCSIB TP5 2015
# Nom: Dizier Charles
# ****************************

import sys


def decimal_to_base(n, k):
    result = ""
    while n > 0:
        n, r = divmod(n, k)
        result = str(r) + result
    return result


def base_to_decimal(s, k):
    result = 0
    for p, t in enumerate(reversed(s)):
        result += int(t) * (k ** p)
    return result


def decimal_to_hexa(n):
    hexa = "0123456789ABCDEF"
    result = ""
    while n > 0:
        n, r = divmod(n, 16)
        result = hexa[r] + result
    return result


def hexa_to_decimal(s):
    hexa = "0123456789ABCDEF"
    result = 0
    for p, t in enumerate(reversed(s.upper())):
        result += hexa.index(t) * (16 ** p)
    return result


def notacompl(z, nb):
    if z >= 0:
        res = decimal_to_base(z, 2)
        res = "0" * (nb - len(res)) + res
        return res
    else:
        return decimal_to_base(2 ** nb + z, 2)


def notacompl_to_decimal(compl):
    if compl[0] == "1":
        not_compl = ""
        for i in compl:
            not_compl += "0" if i == "1" else "1"
        return -(base_to_decimal(not_compl, 2) + 1)
    else:
        return base_to_decimal(compl, 2)


def sontegaux(a, b):
    return abs(a - b) < sys.float_info.epsilon


def calculserie():
    S, old_S, k = 0, -1, 0
    while not sontegaux(S, old_S):
        k += 1
        old_S = S
        S += 0.25 ** k
    return S, k


if __name__ == "__main__":
    print(notacompl(0, 8))
    print(notacompl(2, 8))
    print(notacompl(-2, 8))
    print(notacompl(1, 8))
    print(notacompl(-1, 8))
    print(notacompl(-127, 8))
    print(notacompl(-128, 8))
    print(notacompl_to_decimal("00000010"))
    print(calculserie())

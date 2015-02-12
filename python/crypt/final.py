#!/usr/bin/env python3
# -*- coding: utf_8 -*-


def factoriser(n):
    div = []
    for d in range(2, int(n ** .5)+1):
        while n % d == 0:
            n = n // d
            div.append(d)
    if n != 1:
        div.append(n)
    return div


def est_premier(n):
    return len(factoriser(n)) == 1


def decomposer(n):
    print(n, "=", ".".join([str(i) for i in factoriser(n)]))


def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def bezout(a, b):
    x, y, u, v = 1, 0, 0, 1
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return x, y, b


def dec2bin(n):
    return dec2base(n, 2)


def dec2base(n, k):
    b = ""
    while n > 0:
        n, r = divmod(n, k)
        b = str(r) + b
    return b


def puissance(x, k, n):
    res = 1
    while k:
        k, r = divmod(k, 2)
        if r:
            res = (res % n * x % n) % n
        x = ((x % n) * (x % n)) % n
    return res


def crible(n):
    if n < 2:
        return []
    tab, tab[0], tab[1] = [True] * (n + 1), False, False
    for i in range(n+1):
        if tab[i]:
            tab[i ** 2::i] = [False] * len(tab[i ** 2::i])
    return [i for i in range(n+1) if tab[i]]

if __name__ == "__main__":
    print(puissance(4343579987, 7655229869897684632, 9867868653532))
    print(crible(101))

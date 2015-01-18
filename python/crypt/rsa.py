#!/usr/bin/env python3
# -*- coding: utf_8 -*-


def exp_pow(x, n, mod):
    res = 1
    while n:
        n, r = divmod(n, 2)
        if r:
            res = (res * x) % mod
        x = x * x % mod
    return res


def factorise(n):
    div = []
    for d in range(2, int(n ** .5)+1):
        while n % d == 0:
            n = n // d
            div.append(d)
    if n != 1:
        div.append(n)
    return div


def pretty_decompose(n):
    div = factorise(n)
    print(n, "=", ".".join([str(i) for i in div]))


def is_prime(n):
    for t in [2, 3, 5, 7, 11, 13, 17]:
        if exp_pow(t, n-1, n) != 1:
            return False
    return len(factorise(n)) == 1

if __name__ == "__main__":
    primes = []
    for n in range(10000001, 20000000, 2):
        if is_prime(n):
            primes.append(n)
    print(len(primes))

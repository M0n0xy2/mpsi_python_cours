#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import string


def quick_pow(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return quick_pow(x * x, n // 2)
    else:
        return x * quick_pow(x * x, (n - 1) // 2)


def exp_pow(x, n):
    res = 1
    puiss = x
    while n:
        q, r = divmod(n, 2)
        if r:
            res *= puiss
        puiss *= puiss
        n = q
    return res


def to_bin(num):
    b = ""
    while num > 0:
        num, r = divmod(num, 2)
        b = str(r) + b
    return b


def to_base(num, base):
    b = ""
    while num > 0:
        num, r = divmod(num, base)
        b = str(r) + b
    return b


def cesar_encode(msg, key):
    enc_msg = ""
    for c in msg:
        if c in string.ascii_lowercase:
            pos = (ord(c) - 97 + key) % 26
            enc_msg += chr(pos + 97)
        elif c in string.ascii_uppercase:
            pos = (ord(c) - 65 + key) % 26
            enc_msg += chr(pos + 65)
        else:
            enc_msg += c
    return enc_msg


def cesar_decode(enc_msg, key):
    return cesar_encode(enc_msg, -key)


if __name__ == "__main__":
    print(cesar_decode(cesar_encode("my name is Paul ! Paul Cacheux", 15), 15))

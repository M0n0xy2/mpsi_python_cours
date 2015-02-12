#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import unicodedata

def factoriser(n):
    def generator():
        yield 2
        for i in range(3, int(n ** .5) + 1, 2):
            yield i

    facteurs, valuations = [], []

    for d in generator():
        if n % d == 0:
            facteurs.append(d)
            valuations.append(0)
            while n % d == 0:
                valuations[-1] += 1
                n //= d
    if n != 1:
        facteurs.append(n)
        valuations.append(1)
    return [(facteurs[i], valuations[i]) for i in range(len(facteurs))]


def decomposer(n):
    print(n, "=", " * ".join(["{}**{}".format(a, b) for a, b in factoriser(n)]))

def decomposer_v2(n):
    div = factoriser(n)
    meg_div = [elem for tup in div for elem in tup]
    print(n, "=", ("{}^{} * " * len(div)).format(*meg_div)[:-3])


def msg2num(msg):
    letters_table = " ABCDEFGHIJKLMNOPQRSTUVWXYZ',-.?"
    unicodedata.normalize('NFKD', msg).encode('ascii', 'ignore')
    msg = msg.upper() + " " * ((-len(msg)) % 10)
    pieces = [msg[i:i+10] for i in range(0, len(msg), 10)]
    num = []
    for piece in pieces:
        s = 0
        for i, letter in enumerate(piece):
            if letter not in letters_table:
                letter = "?"
            s += letters_table.index(letter) * 10 ** i 
        num.append(s)
    return num

def num2msg(num):
    letters_table = " ABCDEFGHIJKLMNOPQRSTUVWXYZ',-.?"
    msg = ""
    for piece in num:
        for i in reversed(range(10)):
            msg += letters_table[piece // (10 ** i)]
    return msg


if __name__ == "__main__":
    a = msg2num("COMMENT EST VOTRE BLANQUéTTE ?")
    print(num2msg(a))


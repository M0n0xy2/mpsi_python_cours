# -*- coding: UTF-8 -*-

import sys
from math import sqrt


def Mat():
    for i in range(5):
        print("[" + "0"*i + "1" + "0"*(4-i) + "]")


def mystere(mot):
    n = len(mot)
    A = "+" + "-"*(n+2) + "+"
    B = "| "
    for c in mot[::-1]:
        B = B + c
    B = B + " |"
    print(A + "\n" + B + "\n" + A)


def Somme(a, b):
    somme = 0
    for k in range(a, b+1):
        somme += k
    print(somme)


def mult(a, b):
    prod = 0
    for _ in range(b):
        prod += a
    return prod


def grille(L=None):
    if L is None:
        L = [" " for _ in range(9)]

    n = int(sqrt(len(L)))
    A = " {} |" * (n-1) + " {} \n"
    B = "---+" * (n-1) + "---\n"
    grille = A + (B + A) * (n-1)
    print(grille.format(*L))


def main(argv):
    Mat()
    mystere("par exemple")
    Somme(1, 10)
    print(mult(9, 9))
    grille([c for c in "parapluie"])
    grille(list(range(1, 5)))
    grille()

if __name__ == '__main__':
    main(sys.argv[1:])

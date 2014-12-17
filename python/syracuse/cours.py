#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import sys

def f(n):
    return n // 2 if n % 2 == 0 else 3*n + 1

def vol(n):
    L = [n]
    while n != 1:
        n = f(n)
        L.append(n)
    return L

def temps_de_vol(n):
    return len(vol(n))-1

def hauteur_de_vol(n):
    return max(vol(n))

def maximum_temps_de_vol(max=1000):
    record = 1
    for n in range(1, max+1):
        t = temps_de_vol(n)
        if t > record:
            record = t
            auteur = n
    print("Record de temps de vol : {} Auteur : {}".format(record, auteur))

def maximum_hauteur_de_vol(max=1000):
    record = 1
    for n in range(1, max+1):
        t = hauteur_de_vol(n)
        if t > record:
            record = t
            auteur = n
    print("Record en hauteur : {} Auteur : {}".format(record, auteur))

def main(argv):
    n = 7
    print(vol(n))
    print(temps_de_vol(n))
    print(hauteur_de_vol(n))

if __name__ == "__main__":
    main(sys.argv[1:])

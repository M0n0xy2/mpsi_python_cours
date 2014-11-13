# -*- coding: UTF-8 -*-

import sys


def encadre(phrase):
    ws = phrase.split()
    t = "+" + "+".join(["-"*(len(w)+2) for w in ws]) + "+"
    print(t, "| " + " | ".join(ws) + " |", t, sep="\n")


def main(argv):
    encadre("salut je m'appelle Paul Cacheux")

if __name__ == '__main__':
    main(sys.argv[1:])

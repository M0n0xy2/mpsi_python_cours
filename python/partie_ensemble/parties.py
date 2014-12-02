#!/usr/bin/env python3

import sys

class MathSet(list):
    def __str__(self):
        if len(self) == 0:
            # return "\N{EMPTY SET}"
            return "\u2205"
        else:
            return "{{{}}}".format(", ".join([str(elem) for elem in self]))


def parties_compr(seq):
    return MathSet([MathSet([seq[j] for j in range(0, len(seq)) if ((i >> j) & 1) == 1]) for i in range(0, 2**len(seq))])

def parties(seq):
    p = MathSet()
    for i in range(0, 2**len(seq)):
        s = MathSet()
        for j in range(0, len(seq)):
            if ((i >> j) & 1) == 1:
                s.append(seq[j])
        p.append(s)
    return p


def main(argv):
    print(parties_compr([1, 2, 3]))
    print(parties([1, 2, 3]))

if __name__ == "__main__":
    main(sys.argv[1:])

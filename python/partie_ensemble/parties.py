#!/usr/bin/env python3

import sys


def print_set_man(parts):
    raw = repr(parts)
    to_print = str()
    for c in raw:
        if c == "[":
            to_print += "{"
        elif c == "]":
            if to_print[-1] == "{":
                to_print = to_print[:-1] + "\u2205"
            else:
                to_print += "}"
        else:
            to_print += c
    print(to_print)

def print_set(parts):
    print(repr(parts).replace("[", "{").replace("]", "}").replace("{}", "\u2205"))


def P(seq):
    return P_test(seq)


def P_compr(seq):
    return [[seq[j] for j in range(0, len(seq)) if ((i >> j) & 1) == 1] for i in range(0, 2**len(seq))]


def P_man(seq):
    p = []
    for i in range(0, 2**len(seq)):
        s = []
        for j in range(0, len(seq)):
            if ((i >> j) & 1) == 1:
                s.append(seq[j])
        p.append(s)
    return p


def P_prof(E):
    Res = [[]]
    for x in E:
        S = []
        for A in Res:
            S += [A + [x]]
        Res += S
    return Res


def P_test(E):
    Res = [[]]
    for x in E:
        for A in Res:
            A.append(x)
            Res.append(A)
    return Res


def main(argv):
    print_set(P([1, 2]))
    print_set(P([]))
    print_set(P([1, 2, 3, 4]))

if __name__ == "__main__":
    main(sys.argv[1:])

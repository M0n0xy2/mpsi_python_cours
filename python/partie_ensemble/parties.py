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

def parties(seq):
    p = []
    for i in range(0, 2**len(seq)):
        s = []
        for j in range(0, len(seq)):
            if ((i >> j) & 1) == 1:
                s.append(seq[j])
        p.append(s)
    return p


def main(argv):
    print_set(parties([1, 2, 3]))
    print_set(parties([[[[]]]]))

if __name__ == "__main__":
    main(sys.argv[1:])
